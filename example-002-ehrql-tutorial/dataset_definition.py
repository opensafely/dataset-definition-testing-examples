from ehrql import create_dataset, codelist_from_csv, days, show
from ehrql.tables.core import patients, practice_registrations, clinical_events, medications

index_date = "2024-03-31"

diabetes_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-dm_cod.csv", column="code")
resolved_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-dmres_cod.csv", column="code")
proteinuria_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-prt_cod.csv", column="code")
microalbuminuria_codes = codelist_from_csv("codelists/nhsd-primary-care-domain-refsets-mal_cod.csv", column="code")
ace_codes = codelist_from_csv("codelists/opensafely-ace-inhibitor-medications.csv", column="code")
arb_codes = codelist_from_csv("codelists/opensafely-angiotensin-ii-receptor-blockers-arbs.csv", column="code")

previous_events = clinical_events.where(clinical_events.date.is_on_or_before(index_date))
recent_meds = medications.where(medications.date.is_on_or_between(index_date - days(180), index_date))

aged_17_or_older = (index_date - patients.date_of_birth).years >= 17
was_alive = patients.date_of_death.is_null() | (patients.date_of_death < index_date)
was_registered = (
    practice_registrations.where(practice_registrations.start_date <= index_date)
    .except_where(practice_registrations.end_date < index_date)
    .exists_for_patient()
)

last_diagnosis_date = (
    previous_events
    .where(clinical_events.snomedct_code.is_in(diabetes_codes))
    .sort_by(clinical_events.date)
    .last_for_patient()
    .date
)
last_resolved_date = (
    previous_events
    .where(clinical_events.snomedct_code.is_in(resolved_codes))
    .sort_by(clinical_events.date)
    .last_for_patient()
    .date
)

has_unresolved_diabetes = last_diagnosis_date.is_not_null() & (
    last_resolved_date.is_null() | (last_resolved_date < last_diagnosis_date)
)

on_register = aged_17_or_older & was_alive & was_registered & has_unresolved_diabetes

has_proteinuria_diagnosis = (
    previous_events
    .where(clinical_events.snomedct_code.is_in(proteinuria_codes))
    .exists_for_patient()
)

has_microalbuminuria_diagnosis = (
    previous_events
    .where(clinical_events.snomedct_code.is_in(microalbuminuria_codes))
    .exists_for_patient()
)

has_arb_treatment = (
    recent_meds
    .where(medications.dmd_code.is_in(arb_codes))
    .exists_for_patient()
)

has_ace_treatment = (
    recent_meds
    .where(medications.dmd_code.is_in(ace_codes))
    .exists_for_patient()
)

dataset = create_dataset()
dataset.define_population(on_register)

dataset.prt_or_mal = has_proteinuria_diagnosis | has_microalbuminuria_diagnosis
dataset.ace_or_arb = has_arb_treatment | has_ace_treatment

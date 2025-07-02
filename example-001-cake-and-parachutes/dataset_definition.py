from ehrql import create_dataset, codelist_from_csv
from ehrql.tables.core import patients, medications, clinical_events

cake_codelist = codelist_from_csv('codelists/cake.csv', column = 'code')
parachuting_codelist = codelist_from_csv('codelists/parachuting.csv', column = 'code')

dataset = create_dataset()

index_date = "2020-03-31"

is_within_age_range = (patients.age_on(index_date) < 80) & (patients.age_on(index_date) > 17)

dataset.define_population(is_within_age_range)

has_history_of_cake = medications.where(
    medications.dmd_code.is_in(cake_codelist)
    ).where(
    medications.date.is_before(index_date)
    ).exists_for_patient()

has_history_of_parachuting = clinical_events.where(
    clinical_events.snomedct_code.is_in(parachuting_codelist)
    ).where(
    clinical_events.date.is_before(index_date)
    ).exists_for_patient()

dataset.sex = patients.sex
dataset.age = patients.age_on(index_date)
dataset.cake = has_history_of_cake
dataset.parachuting = has_history_of_parachuting
from ehrql import create_dataset, codelist_from_csv, days, show
from ehrql.tables.core import patients, clinical_events, medications

def make_dataset(index_date, codelist, codelist_type):
    dataset = create_dataset()

    was_born = patients.date_of_birth < index_date
    
    has_not_died = (patients.date_of_death.is_null()) | (patients.date_of_death > index_date)

    dataset.define_population(was_born & has_not_died)

    dataset.sex = patients.sex
    dataset.age = patients.age_on(index_date)

    if codelist_type == "medications":
        has_history_of_medication = medications.where(
            medications.dmd_code.is_in(codelist)
            ).where(
            medications.date.is_before(index_date)
            ).exists_for_patient()
        dataset.medication_history = has_history_of_medication

    elif codelist_type == "clinical_events":
        has_history_of_clinical_event = clinical_events.where(
            clinical_events.snomedct_code.is_in(codelist)
            ).where(
            clinical_events.date.is_before(index_date)
            ).exists_for_patient()
        dataset.clinical_event_history = has_history_of_clinical_event

    else:
        # we passed something in to the dataset function that wasn't 
        # "medications" or "clinical_events". Raise an error and include the
        # bad codelist_type.
        raise Exception(f"Unknown codelist_type passed to dataset function: {codelist_type}")
    
    return dataset
    
from datetime import date
from dataset_definition import dataset

test_data = {
    # Expected in population with unresolved diabetes and a proteinuria diagnosis
    1: {
        "patients": {"date_of_birth": date(1970, 1, 1), "sex": "female"},
        "medications": [],
        "clinical_events": [
            {
                "date": date(2015, 3, 3),
                "snomedct_code": "313436004",
            },
            {
                "date": date(2017, 3, 3),
                "snomedct_code": "762261001",
            },
        ],
        "practice_registrations": [
            {
                "start_date": date(2015, 1, 1),
                "practice_pseudo_id": 12345,
            }
        ],
        "expected_in_population": True,
        "expected_columns": {
            "prt_or_mal": True,
            "ace_or_arb": False,
        },
    },
    # Not expected in population, due to revolved diabetes that unresolved AFTER the index date
    2: {
        "patients": {"date_of_birth": date(1950, 1, 1), "sex": "female"},
        "medications": [],
        "clinical_events": [
            {
                "date": date(2015, 3, 3),
                "snomedct_code": "313436004",
            },
            {
                "date": date(2016, 3, 3),
                "snomedct_code": "315051004",
            },
            {
                # This doesn't affect dataset population prsence because it happened after the index date
                "date": date(2024, 10, 3),
                "snomedct_code": "313436004",
            },
        ],
        "practice_registrations": [
            {
                "start_date": date(2013, 1, 1),
                "end_date": date(2014, 3, 3),
                "practice_pseudo_id": 12345,
            },
            {
                "start_date": date(2014, 5, 1),
                "practice_pseudo_id": 54321,
            },
        ],
        "expected_in_population": False,
    },
    # Expected in population with [criteria]
    3: {
        "patients": [{"date_of_birth": date(1950, 1, 1), "sex": "male"}],
        "medications": [],
        "clinical_events": [],
        "practice_registrations": [],
        "expected_in_population": False,
    },
    # Not expected in population
    4: {
        "patients": [{"date_of_birth": date(2010, 1, 1)}],
        "medications": [],
        "clinical_events": [],
        "practice_registrations": [],
        "expected_in_population": False,
    },
}

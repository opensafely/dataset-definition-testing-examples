from datetime import date
from dataset_definition import dataset

test_data = {
    # Expected in population, with unresolved diabetes and a proteinuria diagnosis
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
    # Not expected in population, due to revolved diabetes that unresolved AFTER the index date.
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
    # Expected in population with unresolved diabetes, a diagnosis of 
    # # micro-albuminuria, and a recent history of treatment with ACE medications
    3: {
        "patients": [{"date_of_birth": date(1973, 5, 1), "sex": "intersex"}],
        "medications": [
            {
                # ACE prescription within 180 days of index date
                "date": date(2024, 1, 1),
                "dmd_code": "21912111000001107",
            }
        ],
        "clinical_events": [
            {
                # Diabetes diagnosis
                "date": date(2016, 1, 1),
                "snomedct_code": "44054006",
            },
            {
                # MAL diagnosis
                "date": date(2017, 1, 1),
                "snomedct_code": "762261001",
            }
        ],
        "practice_registrations": [
            {
                "start_date": date(2013, 7, 10),
                "practice_pseudo_id": 90210,
            }],
        "expected_in_population": True,
        "expected_columns": {
            "prt_or_mal": True,
            "ace_or_arb": True,
        },
    },
    # Expected in population with unresolved diabetes and a diagnosis of 
    # # micro-albuminuria. However, their history of ACE inhibitor treatment is not recent 
    # enough to count.
    4: {
        "patients": [{"date_of_birth": date(1973, 5, 1), "sex": "intersex"}],
        "medications": [
            {
                # ACE prescription, earlier than 180 days of index date
                "date": date(2018, 1, 1),
                "dmd_code": "21912111000001107",
            }
        ],
        "clinical_events": [
            {
                # Diabetes diagnosis
                "date": date(2016, 1, 1),
                "snomedct_code": "44054006",
            },
            {
                # MAL diagnosis
                "date": date(2017, 1, 1),
                "snomedct_code": "762261001",
            }
        ],
        "practice_registrations": [
            {
                "start_date": date(2013, 7, 10),
                "practice_pseudo_id": 90210,
            }],
        "expected_in_population": True,
        "expected_columns": {
            "prt_or_mal": True,
            "ace_or_arb": False,
        },
    },
    # Not expected in population due to lack of practice registration
    5: {
        "patients": [{"date_of_birth": date(2010, 1, 1)}],
        "medications": [],
        "clinical_events": [],
        "practice_registrations": [],
        "expected_in_population": False,
    },
}

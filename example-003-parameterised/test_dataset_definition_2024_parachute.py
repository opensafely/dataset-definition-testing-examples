from datetime import date
from make_dataset_2024_parachute import dataset

test_data = {
    # Expected in population without history of parachuting
    1: {
        "patients": [
            {
                "date_of_birth": date(1954, 1, 1),
                "sex": "female",
            }
        ],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "female",
            "age": 70,
            "clinical_event_history": False,
        },
    },

    # Expected in population with history of parachuting
    2: {
        "patients": [
            {
                "date_of_birth": date(1974, 1, 1),
                "sex": "male",
            }
        ],
        "medications": [],
        "clinical_events": [
            {
                "date": date(2012, 1, 1),
                "snomedct_code": "242233009",
            }
        ],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "male",
            "age": 50,
            "clinical_event_history": True,
        },
    },

    # Not expected in population (born after index date)
    3: {
        "patients": [
            {
                "date_of_birth": date(2025, 1, 1),
                "sex": "male",
            }
        ],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": False,
    },

    # Not expected in population (died before index date)
    4: {
        "patients": [
            {
                "date_of_birth": date(1932, 1, 1),
                "date_of_death": date(2023, 1, 1),
                "sex": "intersex",
            }
        ],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": False,
    },
}
from datetime import date
from make_dataset_2020_cake import dataset

test_data = {
    # Expected in population without history of cake
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
            "medication_history": False,
        },
    },

    # Expected in population with history of cake
    2: {
        "patients": [
            {
                "date_of_birth": date(1974, 1, 1),
                "sex": "male",
            }
        ],
        "medications": [
            {
                "date": date(2000, 1, 1),
                "dmd_code": "41835611000001109",
            }
        ],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "male",
            "age": 50,
            "medication_history": True,
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
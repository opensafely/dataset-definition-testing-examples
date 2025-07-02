from datetime import date
from dataset_definition import dataset

test_data = {
    # Expected in population with [criteria]
    1: {
        "patients": {"date_of_birth": date(1950, 1, 1), "sex": "female"},
        "medications": [],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {},
    },
    # Expected in population with [criteria]
    2: {
        "patients": {"date_of_birth": date(1950, 1, 1), "sex": "female"},
        "medications": [],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {},
    },
    # Expected in population with [criteria]
    3: {
        "patients": [{"date_of_birth": date(1950, 1, 1), "sex": "male"}],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {},
    },
    # Not expected in population
    4: {
        "patients": [{"date_of_birth": date(2010, 1, 1)}],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": False,
    },
}

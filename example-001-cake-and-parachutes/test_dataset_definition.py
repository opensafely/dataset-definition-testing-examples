from datetime import date
from dataset_definition import dataset

test_data = {
    # Expected in population with both cake and parachuting
    1: {
        "patients": {"date_of_birth": date(1950, 1, 1), "sex": "female"},
        "medications": [
            {
                # First matching medication
                "date": date(2010, 1, 1),
                "dmd_code": "42115611000001109",
            },
            {
                # Latest matching medication before index_date
                "date": date(2020, 1, 1),
                "dmd_code": "42115611000001109",
            },
            {
                # Most recent matching medication, but after index_date
                "date": date(2023, 6, 1),
                "dmd_code": "42115611000001109",
            },
        ],
        "clinical_events": [
            {
                "date": date(2015, 1, 1),
                "snomedct_code": "418565008",
            }
        ],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "female",
            "age": 70,
            "cake": True,
            "parachuting": True,
        },
    },
    # Expected in population with cake but not parachuting
    2: {
        "patients": {"date_of_birth": date(1950, 1, 1), "sex": "female"},
        "medications": [
            {
                # First matching medication
                "date": date(2010, 1, 1),
                "dmd_code": "42115611000001109",
            },
            {
                # Latest matching medication before index_date
                "date": date(2020, 1, 1),
                "dmd_code": "42115611000001109",
            },
            {
                # Most recent matching medication, but after index_date
                "date": date(2023, 6, 1),
                "dmd_code": "42115611000001109",
            },
        ],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "female",
            "age": 70,
            "cake": True,
            "parachuting": False,
        },
    },
    # Expected in population without cake or parachuting
    3: {
        "patients": [{"date_of_birth": date(1950, 1, 1), "sex": "male"}],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": True,
        "expected_columns": {
            "sex": "male",
            "age": 70,
            "cake": False,
            "parachuting": False,
        },
    },
    # Not expected in population
    4: {
        "patients": [{"date_of_birth": date(2010, 1, 1)}],
        "medications": [],
        "clinical_events": [],
        "expected_in_population": False,
    },
}

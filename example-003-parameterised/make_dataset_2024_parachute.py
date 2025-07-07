from ehrql import codelist_from_csv
from dataset_definition import make_dataset

parachuting_codelist = codelist_from_csv('codelists/parachuting.csv', column = 'code')

dataset = make_dataset("2024-01-01", parachuting_codelist, "clinical_events")

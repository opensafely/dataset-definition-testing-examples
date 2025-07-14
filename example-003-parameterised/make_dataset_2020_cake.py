from ehrql import codelist_from_csv
from dataset_definition import make_dataset

cake_codelist = codelist_from_csv('codelists/cake.csv', column = 'code')

dataset = make_dataset("2020-01-01", cake_codelist, "medications")

# extra logic goes here

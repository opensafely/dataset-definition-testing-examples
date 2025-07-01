# dataset-definiton-testing-examples

This repository contains reference examples of [the dataset definition testing functionality of ehrQL](https://docs.opensafely.org/ehrql/how-to/test-dataset-definition/). It is updated on an ongoing basis.

Each example lives in its own directory, and each directory contains a dataset definition (`dataset_definition.py`) and a test file (`test_dataset_definition.py`). To run the tests for a given example, navigate to its directory in the terminal, then run the `assure` ehrQL command:

```
cd example-X-name-of-example
opensafely exec ehrql:v1 assure test_dataset_definition.py
```

# About the OpenSAFELY framework

The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.

Read more at [OpenSAFELY.org](https://opensafely.org).

# Licences
As standard, research projects have a MIT license. 

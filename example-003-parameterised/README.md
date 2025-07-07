This example shows how to use the dataset definition testing functionality when you are working with a dataset dfefinition that is parameterised.

The typical usage pattern for a parameterised datatset definition goes as follows:

- In the `dataset_definition.py` file, you will define a function called `make_dataset` (or similar) that takes input variables (such as a date, or a codelist) and returns a dataset object.
- You'll then import and call this function in another file, likely `dataset_definition_[specific_variables]` or something similar. This file is the file that would be specified in your `project.yaml` as part of your pipeline.
- Then, to test your dataset logic, you'd import the `dataset` object from _that_ file into your test file, rather than from your main parameterised `dataset_definition,py` file.

--

In this directory, the parameterised dataset definition is very simple:
- Find people who were alive at a specific date.
- Record whether they have a specifkind of history.

In this case, the kinds of history we're looking at are of different types - one is medication history, the other is history of clinical events. So, our dataset function needs three inputs:
- index date
- codelist
- codelist type (medication or clinical event).
import great_expectations as gx
import pandas as pd

df = pd.read_csv("data/cleaned/cleaned_ratings.csv")
context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="rating assets")
batch_definition = data_asset.add_batch_definition_whole_dataframe("ratings_batch")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

suite_name = "my_expectation_suite"
suite = gx.ExpectationSuite(name=suite_name)
suite = context.suites.add(suite)


expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="rating", min_value=0, max_value=5
)
suite.add_expectation(expectation)

for column in ["userId", "movieId", "rating"]:
    expectation = gx.expectations.ExpectColumnValuesToNotBeNull(column=column)
    suite.add_expectation(expectation)


expectation = gx.expectations.ExpectCompoundColumnsToBeUnique(
    column_list=["userId", "movieId"]
)
suite.add_expectation(expectation)



expectation_suite = context.suites.get(name=suite_name)
batch_definition = (
    context.data_sources.get("pandas")
    .get_asset("rating assets")
    .get_batch_definition("ratings_batch")
)

definition_name = "my_validation_definition"
validation_definition = gx.ValidationDefinition(
    data=batch_definition, suite=expectation_suite, name=definition_name
)

validation_definition = context.validation_definitions.add(validation_definition)

validation_definition = context.validation_definitions.get(definition_name)
batch_parameters = {"dataframe": df}

validation_results = validation_definition.run(batch_parameters=batch_parameters)

print(validation_results)
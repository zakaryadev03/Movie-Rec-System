import great_expectations as gx
import pandas as pd

df = pd.read_csv("data/cleaned/cleaned_ratings.csv")
context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="rating", min_value=0, max_value=5
)

validation_result = batch.validate(expectation)

print(validation_result)

import pandas as pd

df = pd.read_csv("data/processed/customers_clean.csv")

assert df["customer_id"].is_unique
assert df["spend_30d"].min() >= 0
assert df["country"].isin(["CA","US","UK","UNKNOWN"]).all()

print("All QA checks passed")


import pandas as pd
import numpy as np
import re
import os

RAW = "data/raw/messy_customers.csv"
OUT = "data/processed/customers_clean.csv"
os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv(RAW, parse_dates=["signup_date"])

# Drop duplicate customers
df = df.sort_values("signup_date").drop_duplicates("customer_id")

# Email validation
email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
df["email"] = df["email"].where(df["email"].astype(str).str.match(email_re))

# Age bounds
df["age"] = df["age"].where(df["age"].between(16, 85))

# Country cleanup
df["country"] = df["country"].fillna("").replace("", "UNKNOWN")

# Cap future signup dates
today = pd.Timestamp.today().normalize()
df.loc[df["signup_date"] > today, "signup_date"] = today

# No negative spend
df["spend_30d"] = np.maximum(df["spend_30d"], 0)

df.to_csv(OUT, index=False)
print("Cleaned data written")

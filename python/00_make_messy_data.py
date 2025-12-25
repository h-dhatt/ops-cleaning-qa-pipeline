
import numpy as np
import pandas as pd
import os

rng = np.random.default_rng(1)
os.makedirs("data/raw", exist_ok=True)

n = 2000
df = pd.DataFrame({
    "customer_id": range(1, n+1),
    "email": [f"user{i}@example.com" for i in range(1, n+1)],
    "age": rng.integers(14, 90, size=n),
    "country": rng.choice(["CA", "US", "", None, "UK"], size=n),
    "signup_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(-30, 400, size=n), unit="D"),
    "spend_30d": rng.normal(60, 40, size=n).round(2)
})

df.loc[df.sample(40, random_state=2).index, "email"] = "bad_email"
df = pd.concat([df, df.sample(25, random_state=3)])

df.to_csv("data/raw/messy_customers.csv", index=False)
print("Generated messy dataset")

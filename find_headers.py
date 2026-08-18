import pandas as pd
df_raw = pd.read_csv("kenya_counties_official.csv", nrows = 10)
for index,row in df_raw.iterrows():
    print(f"Row {index}: {row.values}")


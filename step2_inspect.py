import pandas as pd

# Load our pristine local dataset
df = pd.read_csv("kenya_counties_official.csv")

print("--- DATASET SHAPE (Rows, Columns) ---")
print(df.shape)

print("\n--- DATA TYPES & NULL CHECK ---")
print(df.info())

print("\n--- FIRST 5 ROWS ---")
print(df.head())
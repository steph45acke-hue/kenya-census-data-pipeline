import pandas as pd

print("1. Downloading and formatting the Kenya census dataset...")

url = "https://raw.githubusercontent.com/GichanaMayaka/Kenya-Dataset/main/kenya-population-land-area-population-density_by_county.csv"

try:
    # Skip the first 6 metadata rows and map explicit columns
    df = pd.read_csv(url, skiprows=6, header=None)
    df.columns = ["County", "Population", "Land_Area_SqKm", "Population_Density"]
    
    # Drop Row 0 (duplicate text header) and Row 1 (national total 'Kenya')
    df = df.drop([0, 1]).reset_index(drop=True)
    
    print("-> Success! Data loaded, headers mapped, and top artifacts dropped.")
except Exception as e:
    print(f"-> Error: {e}")
    exit()

# Save the pristine local version
local_filename = "kenya_counties_official.csv"
df.to_csv(local_filename, index=False)

print(f"\n--- FIRST 5 ROWS OF PRISTINE DATA ---")
print(df.head())
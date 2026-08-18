import pandas as pd

# Load our pristine dataset
df = pd.read_csv("kenya_counties_official.csv")

print("==========================================")
print(" KENYA CENSUS ANALYTICS & SUMMARY REPORT")
print("==========================================")

# 1. Basic Aggregations
total_population = df["Population"].sum()
total_land_area = df["Land_Area_SqKm"].sum()

print(f"\nTotal National Population: {total_population:,}")
print(f"Total Land Area: {total_land_area:,.2f} Sq. Km")

# 2. Top 5 Most Populated Counties
top_5_populated = df.sort_values(by="Population", ascending=False).head(5)
print("\n--- TOP 5 MOST POPULATED COUNTIES ---")
print(top_5_populated[["County", "Population", "Population_Density"]].to_string(index=False))

# 3. Top 5 Highest Population Density
top_5_dense = df.sort_values(by="Population_Density", ascending=False).head(5)
print("\n--- TOP 5 HIGHEST DENSITY COUNTIES ---")
print(top_5_dense[["County", "Population_Density", "Land_Area_SqKm"]].to_string(index=False))

print("\n==========================================")
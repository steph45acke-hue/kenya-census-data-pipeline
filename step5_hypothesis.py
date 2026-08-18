import pandas as pd
from scipy import stats

print("1. Loading dataset for hypothesis testing...")
df = pd.read_csv("kenya_counties_official.csv")

# Let's define a list of major metropolitan/densely urbanized counties
urban_hubs = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Kiambu"]

# Split the dataset into two groups: Urban Hubs vs. Other Counties
group_urban = df[df["County"].isin(urban_hubs)]["Population_Density"]
group_others = df[~df["County"].isin(urban_hubs)]["Population_Density"]

print("2. Running Independent Two-Sample T-Test...")
# We use equal_var=False (Welch's t-test) since population densities vary widely in variance
t_stat, p_value = stats.ttest_ind(group_urban, group_others, equal_var=False)

print("\n==========================================")
print(" HYPOTHESIS TEST RESULTS")
print("==========================================")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.6f}")

# Conclusion threshold (alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject the Null Hypothesis ($H_0$).")
    print("Conclusion: There IS a statistically significant difference in population density between urban hubs and other counties.")
else:
    print("\nResult: Fail to Reject the Null Hypothesis ($H_0$).")
    print("Conclusion: There is NO statistically significant difference.")
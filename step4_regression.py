import pandas as pd
import statsmodels.api as sm

print("1.loading dataset for regression analysis...")
df = pd.read_csv("kenya_counties_official.csv")

X = df["Land_Area_SqKm"]
Y = df["Population"]

X = sm.add_constant(X)
print("2.fitting the ordinary least(OLS) regression model...")
model = sm.OLS(Y,X).fit()


print("\n==============================")
print(" REGRESSION RESULTS SUMMARY")
print("=====================================")
print(model.summary())

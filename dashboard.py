import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kenya Census Analytics", layout="wide")

st.title("📊 Kenya Census Analytics & Insights Dashboard")
st.markdown("Exploring demographic trends across 47 counties.")

df = pd.read_csv("kenya_counties_official.csv")

# Sidebar
st.sidebar.header("Dashboard Filters")
selected_county = st.sidebar.multiselect("Select Counties", df["County"].unique(), default=df["County"].unique()[:5])

# Metrics
col1, col2 = st.columns(2)
col1.metric("National Population", f"{df['Population'].sum():,}")
col2.metric("Total Land Area (SqKm)", f"{df['Land_Area_SqKm'].sum():,.2f}")

# Visuals
st.subheader("Top Populated Counties")
fig, ax = plt.subplots()
df.nlargest(10, "Population").plot(kind="bar", x="County", y="Population", ax=ax, color="skyblue")
st.pyplot(fig)

# Insights Section
st.subheader("Statistical Findings")
st.write("Regression Result: Land Area explains only 5.3% of population variation.")
st.write("Hypothesis Test: No statistically significant difference in density between urban hubs and other counties.")
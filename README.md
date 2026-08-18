# 🇰🇪 Kenya Census Data Pipeline & Analytics

This project provides a complete, end-to-end data science workflow designed to turn raw, messy government data tables into pristine, actionable insights for all 47 Kenyan counties. We built this to show how rigorous data engineering and statistical analysis can be applied to real-world demographic challenges.

---

## 📋 What The Project Does & Problems Involved

* **The Problems Involved:** When you download raw demographic data straight from official government portals (like the 2019 Kenya Population and Housing Census), it is full of friction. The files contain messy metadata, unwanted header rows, hidden NaN values, unaligned columns, and formatting artifacts that instantly break standard data processing scripts. Furthermore, raw numbers alone don't explain underlying demographic realities—such as whether a county's physical size dictates its population or if major urban hubs are statistically distinct from rural regions.
* **What The Project Does:** This project automates the entire Extract, Transform, Load (ETL) pipeline using Python. It cleans and structures the dataset across all 47 Kenyan counties, computes key population metrics, runs advanced econometric modeling, and builds an interactive web interface to visualize the findings.

---

## 🎯 Why We Built It & Solution Offered

* **Why We Built It:** We wanted to bridge the gap between raw public records and actionable quantitative insights. Too often, data projects stop at basic cleaning; we wanted a complete, end-to-end portfolio piece that proves how rigorous data science and statistical testing apply to real-world demographics.
* **Solution Offered:** This repository offers a clean, reproducible, and fully documented workflow. It turns messy government spreadsheets into pristine structured data (`kenya_counties_official.csv`), automates statistical hypothesis testing, and provides an interactive Streamlit dashboard so anyone can explore Kenya's demographic distribution instantly.

---

## 🛠️ The Technology Used

* **Python:** The core programming language used for scripting and backend logic.
* **Pandas & NumPy:** For data manipulation, dataframe cleaning, handling missing values, and numerical operations.
* **Statsmodels & SciPy:** For advanced statistical analysis, including Ordinary Least Squares (OLS) regression and Welch's two-sample independent t-tests.
* **Matplotlib & Streamlit:** For data visualization and building an interactive front-end web dashboard.
* **Git & GitHub:** For version control, repository management, and project documentation.

---

## 📸 Step-by-Step Execution & Visual Walkthrough

Here is a step-by-step visual breakdown of how the project comes together across our execution pipeline, specifically laid out so any recruiter reviewing the repository can follow along visually:

### 1. Data Ingestion & Initial Cleaning
* **What you are seeing:** Running `step1_download.py` connects to the raw data source. Early iterations show messy metadata rows (`Unnamed: 0`, title text, and `NaN` values). Through iterative script refinement, we drop unwanted artifacts, explicitly map proper headers, and output a pristine structured dataset containing `County`, `Population`, `Land_Area_SqKm`, and `Population_Density`.

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(121).png" width="100%">
<em>Initial raw output showing messy metadata and unnamed columns during script development.</em>
<br><br>

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(125).png" width="100%">
<em>Final pristine data structure after the cleaning script runs successfully.</em>
<br>

---

### 2. Data Inspection & Summary Analysis
* **What you are seeing:** Running `step2_inspect.py` confirms our dataset shape is exactly 47 rows (representing all 47 counties) with clean integer and float data types and zero null values. Running `step3_analysis.py` outputs top-level national totals (e.g., total national population of ~47.56 million and total land area of ~580,876 Sq. Km) alongside rankings for top populated counties and highest density regions.

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(126).png" width="100%">
<em>Data inspection terminal showing the 47-row shape and verified column data types.</em>
<br><br>

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(127).png" width="100%">
<em>Summary analytics report displaying national totals and top populated/densest counties.</em>
<br>

---

### 3. Econometric Regression Analysis
* **What you are seeing:** The output of our Ordinary Least Squares (OLS) regression model (`step4_regression.py`), testing whether a county's land area predicts its population size.
* **The Human Explanation:** 
  * **$R^2$ = 0.053 (5.3%):** Land area explains only about 5.3% of the variation in population across Kenyan counties. Large geographic counties (like Turkana or Marsabit) are arid with low populations, while small counties (like Nairobi or Mombasa) have massive populations packed into tight spaces.
  * **P-Value = 0.120:** Since this is above our standard 0.05 threshold, there is **no statistically significant linear relationship** between a county's land area and its population.

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(128).png" width="100%">
<em>OLS Regression results: The high P-value indicates no statistically significant linear relationship.</em>
<br>

---

### 4. Statistical Hypothesis Testing
* **What you are seeing:** The results of our Welch's two-sample independent t-test (`step5_hypothesis.py`), which compares population densities between major urban economic hubs (Nairobi, Mombasa, Kisumu, Nakuru, Kiambu) and the rest of the country.
* **The Human Explanation:** 
  * **P-Value = 0.1316:** Since $p > 0.05$, we **Fail to Reject the Null Hypothesis**. 
  * Even though big cities *feel* overwhelmingly dense, the extreme statistical spread and high variance across the rest of the country mean we cannot prove a mathematically significant difference in density groups at the 5% significance level. In data science, proving *why* an assumption fails is just as valuable as confirming one!

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(129).png" width="100%">
<em>Welch’s T-Test results: Failing to reject the null hypothesis.</em>
<br>

---

### 5. Interactive Web Dashboard
* **What you are seeing:** The local Streamlit web application running in the browser (`localhost:8501`), rendering dynamic bar charts and summaries straight from our processed CSV data.

<br>
<img src="https://raw.githubusercontent.com/steph45acke-hue/kenya-census-data-pipeline/main/Screenshot%20(130).png" width="100%">
<em>The interactive Streamlit dashboard running locally in the browser.</em>
<br>

---

## 💡 Skills Learnt and Used

* **Data Wrangling & ETL:** Parsing messy CSV files, handling headers, aligning columns, and enforcing strict data type schemas in Pandas.
* **Econometric Modeling:** Implementing Ordinary Least Squares (OLS) regression, interpreting R-squared values, p-coefficients, and standard errors.
* **Inferential Statistics:** Executing Welch's independent t-tests to evaluate group variances and draw valid statistical conclusions.
* **Front-End Deployment:** Bridging backend Python scripts with interactive user interfaces using Streamlit.
* **Technical Documentation:** Writing professional, human-readable GitHub project documentation and structuring clean project repositories.

---

## 🚀 How to Use or Run It

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/steph45acke-hue/kenya-census-data-pipeline.git](https://github.com/steph45acke-hue/kenya-census-data-pipeline.git)
Navigate into the project directory:

Bash
cd kenya-census-data-pipeline
Install the required dependencies:

Bash
python -m pip install pandas numpy statsmodels scipy streamlit matplotlib
Run the pipeline scripts step-by-step:

Bash
python step1_download.py
python step2_inspect.py
python step3_analysis.py
python step4_regression.py
python step5_hypothesis.py
Launch the interactive Streamlit dashboard:

Bash
python -m streamlit run dashboard.py
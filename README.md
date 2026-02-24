# AtliQo Credit Card -- Customer Analysis, Campaign Design & A/B Testing

## 📌 Project Overview

This project performs an end-to-end data science workflow for AtliQo's
Credit Card business.\
The goal is to identify the most valuable customer segment, design a
targeted credit card campaign, and measure its effectiveness using A/B
testing and statistical hypothesis testing.

This project includes: - Data extraction from MySQL\
- Saving raw & processed datasets\
- Data cleaning & preprocessing pipelines\
- Exploratory data analysis (EDA)\
- Identifying the target customer segment\
- Campaign design (18--25 age group)\
- Running an A/B Test\
- Hypothesis testing using Z-Test\
- Final business insights and recommendations

------------------------------------------------------------------------

## 📂 Folder Structure

AtliQo Credit Card/ │ ├── notebooks/ │ ├── 01_customers_eda.ipynb │ ├──
02_credit_profiles_eda.ipynb │ ├── 03_transactions_eda.ipynb │ ├──
04_merged_analysis.ipynb │ ├── 05_target_group_analysis.ipynb │ ├──
06_campaign_design.ipynb │ ├── 07_ab_test_analysis.ipynb │ └──
08_hypothesis_testing.ipynb │ ├── src/ │ ├── config.py │ ├──
data_loader.py │ ├── data_saver.py │ └── preprocessors/ │ ├──
customer_preprocessor.py │ ├── credit_preprocessor.py │ └──
transaction_preprocessor.py │ ├── data/ │ ├── raw/ │ └── processed/ │
├── reports/ │ ├── final_summary.md │ └── credit_analysis_dashboard.png
│ ├── requirements.txt └── README.md

------------------------------------------------------------------------

## 🗄️ Data Pipeline Overview

### **1. Load Data from MySQL**

Implemented in `data_loader.py`.

### **2. Save RAW CSV files**

Using `data_saver.py`: - customers_raw.csv\
- credit_profiles_raw.csv
- transactions_raw.csv

### **3. Preprocess Data**

Each dataset has a dedicated preprocessor.

------------------------------------------------------------------------

## 🎯 Target Group Identification (18--25 Age Group)

Analysis revealed: - \~25% of customer base\
- Low credit history\
- Low CC usage\
- High spending in Electronics/Fashion/Beauty

------------------------------------------------------------------------

## 🚀 Campaign Design

A 2-month pilot campaign with: - Cashback\
- ₹200 bonus\
- Zero annual fee

100 customers selected → 40% converted.

------------------------------------------------------------------------

## 🧪 A/B Testing & Hypothesis Testing

Z-test statistically proved the campaign increased average daily
transactions.

------------------------------------------------------------------------

## ▶️ How to Run

1.  Add .env\
2.  Install requirements\
3.  Run:

```{=html}
<!-- -->
```
    python src/main.py

------------------------------------------------------------------------

## 📑 Requirements

pandas, numpy, sqlalchemy, pymysql, python-dotenv, scipy, statsmodels,
matplotlib, seaborn

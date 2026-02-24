# AtliQo Credit Card — Customer Analysis, Campaign Design & A/B Testing

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
[![IBM Data Science](https://img.shields.io/badge/IBM-Data%20Science%20Professional-052FAD?logo=ibm&logoColor=white)](https://www.credly.com/badges/960adb8c-c3ed-4214-8ab4-9528c93bef21/public_url)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
---

## 📌 Project Overview

An end-to-end data science project for **AtliQo's Credit Card** business unit.  
The goal is to identify the most valuable customer segment, design a targeted credit card campaign, and measure its effectiveness using A/B testing and statistical hypothesis testing.

**Key deliverables:**
- Data extraction from MySQL & preprocessing pipelines
- Exploratory Data Analysis (EDA) across 3 datasets
- Target customer segment identification
- Campaign design for the 18–25 age group
- A/B Test execution & Z-Test hypothesis testing
- Final business insights & recommendations

---

## 📁 Project Structure
```
AtliQo Credit Card/
│
├── notebooks/
│   ├── 01_customers_eda.ipynb
│   ├── 02_credit_profiles_eda.ipynb
│   ├── 03_transactions_eda.ipynb
│   ├── 04_merged_analysis.ipynb
│   ├── atliqo_campaign_ab_test_analysis.ipynb
│   
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── data_saver.py
│   └── preprocessors/
│       ├── customer_preprocessor.py
│       ├── credit_preprocessor.py
│       └── transaction_preprocessor.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── final_summary.md
│   └── credit_analysis_dashboard.png
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🗄️ Data Pipeline

| Step | Script | Output |
|------|--------|--------|
| Extract from MySQL | `data_loader.py` | Raw DataFrames |
| Save raw CSVs | `data_saver.py` | `customers_raw.csv`, `credit_profiles_raw.csv`, `transactions_raw.csv` |
| Clean & preprocess | `preprocessors/` | `customers_processed.csv`, `credit_profiles_processed.csv`, `transactions_processed.csv` | 

---

## 🎯 Target Segment — 18–25 Age Group

| Metric | Insight |
|--------|---------|
| Share of customer base | ~25% |
| Credit history | Low / None |
| Current CC usage | Low |
| Top spending categories | Electronics, Fashion, Beauty |

> **Conclusion:** This segment shows high growth potential with the right incentive-based campaign.

---

## 🚀 Campaign Design

A **2-month pilot campaign** was designed specifically for the 18–25 segment:

- 💰 Cashback on every transaction  
- 🎁 ₹200 welcome bonus  
- 🆓 Zero annual fee for Year 1  

**Pilot result:** 100 customers selected → **40% conversion rate**

---

## 🧪 A/B Testing & Hypothesis Testing

| | Control Group | Treatment Group |
|-|--------------|-----------------|
| Campaign offered | ❌ No | ✅ Yes |
| Avg. daily transactions | Baseline | Significantly higher |
| Test used | Z-Test (two-proportion) | |
| Result | **Statistically significant** increase confirmed |

> The campaign successfully increased daily transaction volume at a 95% confidence level.

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/prasanna-vaddeman/atliqo-credit-card-ab-testing-analysis.git
cd atliqo-credit-card-ab-testing-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
# Fill in your MySQL credentials in .env
```

**4. Run the pipeline**
```bash
python src/main.py
```

---

## 📦 Requirements
```
pandas
numpy
sqlalchemy
pymysql
python-dotenv
scipy
statsmodels
matplotlib
seaborn
```

> Install all at once: `pip install -r requirements.txt`

---

## 📑 Key Insights & Recommendations

1. **18–25 is the highest-opportunity segment** — low current usage but high spending intent
2. **Cashback + zero annual fee** is the most effective acquisition lever for this age group
3. **A/B test confirmed** campaign effectiveness — recommend scaling to full customer base
4. **Top categories** (Electronics, Fashion, Beauty) should anchor future reward structures

---

## 👤 Author

**Prasanna Vaddeman**  
[LinkedIn](https://linkedin.com/in/prasanna-vaddeman) · [GitHub](https://github.com/prasanna-vaddeman)

## 🏅 Certifications

<a href="https://coursera.org/share/50232e89cbf231ca37e0ef6f70e12c24" target="_blank">
  <img src="https://images.credly.com/size/150x150/images/660af5e3-77b6-4c80-9e2a-6ef7cb2c5d58/image.png" alt="IBM Data Science Professional Certificate" width="150"/>
</a>

**IBM Data Science Professional Certificate (V3)**  
Issued by IBM · Verified on [Credly](https://www.credly.com/earner/earned/badge/960adb8c-c3ed-4214-8ab4-9528c93bef21)
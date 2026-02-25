# AtliQo Credit Card — Customer Analysis, Campaign Design & A/B Testing

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-1.11+-8CAAE6?logo=scipy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
[![IBM Data Science](https://img.shields.io/badge/IBM-Data%20Science%20Professional%20V3-052FAD?logo=ibm&logoColor=white)](https://coursera.org/share/50232e89cbf231ca37e0ef6f70e12c24)

---

## 📌 Project Overview

An **end-to-end data science project** for AtliQo's Credit Card business unit — from raw MySQL data to statistically validated business recommendations.

The goal is to identify the most valuable customer segment, design a targeted credit card campaign, and measure its effectiveness using **A/B Testing** and **Z-Test hypothesis testing**.

> 💡 **Business Impact:** Identified a high-potential customer segment (18–25 age group), designed a 2-month pilot campaign, and achieved a **40% conversion rate** — statistically validated at 95% confidence level.

---

## 🗂️ Table of Contents

- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Dataset Summary](#-dataset-summary)
- [Data Pipeline](#️-data-pipeline)
- [Target Segment](#-target-segment--1825-age-group)
- [Campaign Design](#-campaign-design)
- [A/B Testing & Hypothesis Testing](#-ab-testing--hypothesis-testing)
- [Key Insights & Recommendations](#-key-insights--recommendations)
- [How to Run](#️-how-to-run)
- [Requirements](#-requirements)
- [Author](#-author)
- [Certifications](#-certifications)

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
│   └── credit_analysis_dashboard.png
│
├── src/
│   ├── preprocessors/
│   │   ├── __init__.py
│   │   ├── customer_preprocessor.py
│   │   ├── credit_preprocessor.py
│   │   └── transaction_preprocessor.py
│   ├── config.py
│   ├── data_loader.py
│   ├── data_saver.py
│   └── data_exporter.py
│
├── data/
│   ├── raw/
│   │   ├── customers_raw.csv
│   │   ├── credit_profiles_raw.csv
│   │   └── transactions_raw.csv
│   └── processed/
│       ├── customers_processed.csv
│       ├── credit_profiles_processed.csv
│       └── transactions_processed.csv
│
├── database/
│   └── E_MasterCardDump.sql
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Summary

| Dataset | Rows | Columns | Source |
|---------|------|---------|--------|
| Customers | 1,000 | 8 → 9 (1 feature engineered) | MySQL |
| Credit Profiles | 1,004 → 1,000 | 6 → 7 (4 duplicates removed) | MySQL |
| Transactions | 500,000 | 7 | MySQL |

---

## 🗄️ Data Pipeline

| Step | Script | Output |
|------|--------|--------|
| 1. Extract from MySQL | `data_loader.py` | Raw DataFrames |
| 2. Save raw CSVs | `data_saver.py` | `data/raw/*.csv` |
| 3. Clean & preprocess | `preprocessors/` | Cleaned DataFrames |
| 4. Save processed CSVs | `data_saver.py` | `data/processed/*.csv` |
| 5. Export back to MySQL | `data_exporter.py` | Tables in `e_master_card` schema |

**Pipeline Output:**
```
=== AtliQo Credit Card Data Pipeline Started ===
✔ customers loaded successfully.        shape: (1000, 8)
✔ credit_profiles loaded successfully.  shape: (1004, 6)
✔ transactions loaded successfully.     shape: (500000, 7)
✔ Saved RAW files to data/raw/
✔ Preprocessing complete
✔ Saved PROCESSED files to data/processed/
✔ Exported all tables to MySQL (schema: e_master_card)
=== Pipeline Completed Successfully ===
```

---

## 🎯 Target Segment — 18–25 Age Group

| Metric | Insight |
|--------|---------|
| Share of customer base | ~25% |
| Credit history | Low / None |
| Current credit card usage | Low |
| Top spending categories | Electronics, Fashion, Beauty |
| Growth potential | **High** |

> **Conclusion:** The 18–25 segment is largely untapped — low existing CC usage but high spending activity signals strong acquisition potential with the right incentive structure.

---

## 🚀 Campaign Design

A **2-month pilot campaign** was designed specifically for the 18–25 segment:

| Offer | Details |
|-------|---------|
| 💰 Cashback | On every transaction |
| 🎁 Welcome Bonus | ₹200 on first use |
| 🆓 Annual Fee | Zero for Year 1 |
| 👥 Pilot Size | 100 customers |
| 📈 Conversion Rate | **40%** |

---

## 🧪 A/B Testing & Hypothesis Testing

| Metric | Control Group | Treatment Group |
|--------|--------------|-----------------|
| Campaign offered | ❌ No | ✅ Yes |
| Avg. daily transactions | Baseline | Significantly higher |
| Test applied | Z-Test (two-proportion) | Z-Test (two-proportion) |
| p-value | > 0.05 (baseline) | < 0.05 ✅ |
| Result | — | **Statistically significant increase confirmed** |

> ✅ The campaign successfully increased daily transaction volume at a **95% confidence level**.

---

## 📑 Key Insights & Recommendations

1. **18–25 is the highest-opportunity segment** — low current usage but strong spending intent across Electronics, Fashion & Beauty
2. **Cashback + zero annual fee** is the most effective acquisition lever for this demographic
3. **A/B test statistically confirmed** campaign effectiveness — recommend scaling to full customer base
4. **Reward structures** should be anchored around top spending categories (Electronics, Fashion, Beauty)
5. **Credit profile gaps** (4 duplicates, low history records) suggest the need for better onboarding data collection

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
# Open .env and fill in your MySQL credentials:
# DB_HOST=localhost
# DB_USER=your_username
# DB_PASSWORD=your_password
# DB_NAME=e_master_card
```

**4. Import the MySQL database**
```bash
mysql -u your_username -p e_master_card < database/E_MasterCardDump.sql
```

**5. Run the full pipeline**
```bash
python main.py
```

**6. Explore notebooks**
```bash
jupyter notebook notebooks/
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
jupyter
```

> Install all at once: `pip install -r requirements.txt`

---

## 👤 Author

**Prasanna Vaddeman**
[LinkedIn](https://linkedin.com/in/prasanna-vaddeman) · [GitHub](https://github.com/prasanna-vaddeman)

---

## 🏅 Certifications

<a href="https://coursera.org/share/50232e89cbf231ca37e0ef6f70e12c24" target="_blank">
  <img src="https://images.credly.com/size/150x150/images/660af5e3-77b6-4c80-9e2a-6ef7cb2c5d58/image.png" alt="IBM Data Science Professional Certificate" width="130"/>
</a>

**IBM Data Science Professional Certificate (V3)**
Issued by **IBM** · Verified on [Coursera](https://coursera.org/share/50232e89cbf231ca37e0ef6f70e12c24)

---

<p align="center">⭐ If you found this project helpful, consider giving it a star on GitHub!</p>

# 🎓 ScholarTrack — Scholarship Application Analytics

A Python-based data analytics project that analyzes scholarship application records and displays insights through an interactive Streamlit dashboard.

## Features
- Data cleaning and duplicate removal
- Missing-value handling
- Application status analysis
- State-wise application charts
- Interactive dashboard with summary metrics
- Downloadable cleaned dataset

## Technologies Used
- Python
- Pandas
- Matplotlib
- Streamlit

## How to Run

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Run the dashboard

```bash
python -m streamlit run app.py
```

### 3. Open in browser

Open the local URL shown in your terminal.

## Project Files
- `app.py` — Interactive dashboard
- `step1_preview.py` — Dataset preview
- `step2_cleaning.py` — Data cleaning
- `step3_analysis.py` — Data analysis and charts
- `requirements.txt` — Required Python packages
- `scholartrack_applications_raw.csv` — Original practice dataset
- `scholartrack_applications_cleaned.csv` — Cleaned dataset
- `status_chart.png` — Application status chart
- `state_chart.png` — State-wise application chart

## Dataset Disclaimer
The dataset contains synthetic sample data created for educational and demonstration purposes. It does not represent verified real scholarship applications.

## Purpose
Created as a practice project to learn Python, data cleaning, data analysis, and dashboard development.

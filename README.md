# 🚀 TrendPulse — Live Trend Data Pipeline

> **Collect • Clean • Analyse • Visualise • Discover Trends 📊**

TrendPulse is a Python-based data pipeline project that transforms live trending data into meaningful insights and visualizations.

The project follows a complete data workflow:

**🌐 Data Collection → 🧹 Data Processing → 🔍 Data Analysis → 📊 Visualization**

---

## 🎯 Project Overview

TrendPulse demonstrates how raw trend data can be collected from an online source, cleaned and processed using Python, analysed to identify patterns, and finally transformed into easy-to-understand visualizations.

The project is divided into four independent tasks, with each Python script representing one stage of the pipeline.

---

## 🔄 Data Pipeline

```text
              🌐 LIVE TREND DATA
                     │
                     ▼
        ┌──────────────────────────┐
        │  1️⃣ DATA COLLECTION      │
        │  task1_data_collection.py│
        └─────────────┬────────────┘
                      │
                      ▼
             📄 trending_data.csv
                      │
                      ▼
        ┌──────────────────────────┐
        │  2️⃣ DATA PROCESSING      │
        │  task2_data_processing.py│
        └─────────────┬────────────┘
                      │
                      ▼
          📄 cleaned_trending_data.csv
                      │
                      ▼
        ┌──────────────────────────┐
        │  3️⃣ DATA ANALYSIS        │
        │  task3_analysis.py       │
        └─────────────┬────────────┘
                      │
                      ▼
             📄 analysis_results.csv
                      │
                      ▼
        ┌──────────────────────────┐
        │  4️⃣ DATA VISUALIZATION   │
        │  task4_visualization.py  │
        └─────────────┬────────────┘
                      │
                      ▼
                📊 INSIGHTS
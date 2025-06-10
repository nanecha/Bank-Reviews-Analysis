# Week_2  Customer Experience Analytics for Fintech Apps
# *Task-1 Data collection and preprocessing* 
Description

- A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews

## Setup
1. Clone the repo: `git clone https://github.com/nanecha/Bank-Reviews-Analysis>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run analysis: `python scripts/run_pipeline.py
4.google play scraping 
- Collecting individual bank Reviews**
 - Normalize Date**
 - data cleaning 
 -sentimental anlasysis
 - visualization
# Task_2 Bank Reviews Sentiment and Thematic Analysis

## Overview
This project analyzes customer reviews from three Ethiopian banking apps (CBE, Dashen, BOA) to extract sentiment and key themes using NLP techniques.

## Features
- **Data Collection**: Scrapes reviews from Google Play Store
- **Sentiment Analysis**: Uses TextBlob and VADER to classify reviews
- **Thematic Analysis**: Identifies common themes using TF-IDF and rule-based clustering
- **Visualization**: Generates sentiment distributions and word clouds 
## Dependenceis 
- See requirement.text 
# Workflow
## 1. Data Collection:

python
banks = ['com.combanketh.mobilebanking', 
        'com.dashen.dashensuperapp',
        'com.boa.boaMobileBanking']
reviews = fetch_reviews(banks)
## 2. Preprocessing:

- Cleans text (lowercase, remove punctuation)
- Tokenization and lemmatization
- Handles missing values
- Analysis:
   - Sentiment classification (Positive/Negative/Neutral)
   - TF-IDF keyword extraction
    - Theme clustering (Account Access, Transactions, UI/UX etc.)
- Visualization:
     - Sentiment distribution charts
- Word clouds for positive reviews

## Outputs
  - CSV files with cleaned data and sentiment scores
- Visual reports:
- Sentiment by bank and rating
- Top keywords in positive/negative reviews
- Thematic analysis results
# Task-3 stored cleaned in oracle 
   
# Netflix Dataset Exploration

## Overview

This project performs Exploratory Data Analysis (EDA) on the Netflix Movies and TV Shows dataset.

The objective is to analyze Netflix content and discover insights such as:

* Distribution of Movies vs TV Shows
* Top content-producing countries
* Ratings distribution
* Release year trends
* Movie duration analysis
* Missing value handling

This project is part of my daily Machine Learning & Data Science learning journey to strengthen concepts through small practical projects.

---

# Problem Statement

Netflix contains thousands of movies and TV shows from different countries, genres, and ratings.

The goal of this project is to clean, analyze, and visualize the dataset to extract meaningful insights and practice fundamental Data Science concepts like:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Handling Missing Values
* Feature Engineering

---

# Dataset

Dataset Used:
Netflix Movies and TV Shows Dataset

Source:
Kaggle

Dataset Link:
https://www.kaggle.com/datasets/shivamb/netflix-shows

Dataset File:

```bash
netflix_titles.csv
```

---

# Technologies Used

* Python
* Pandas
* Matplotlib

---

# Concepts Covered

## Data Cleaning

* Handling missing values
* Removing unwanted categories
* Cleaning categorical data

## Exploratory Data Analysis (EDA)

* Country-wise content analysis
* Ratings analysis
* Release year trends

## Visualization

* Pie Charts
* Bar Charts
* Histograms
* Line Charts

## Feature Engineering

* Extracting movie duration
* Datetime conversion
* Creating derived columns

---

# Project Structure

```bash
day-01-netflix-analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── screenshots/
│
├── netflix_analysis.ipynb
├── netflix_analysis.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <your-repository-link>
```

Move into the project folder:

```bash
cd day-01-netflix-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# How to Run

Run the Python file:

```bash
python netflix_analysis.py
```

OR open the notebook:

```bash
jupyter notebook
```

---

# Analysis Performed

## 1. Missing Values Analysis

* Identified null values in dataset
* Cleaned missing country values
* Removed unwanted "Unknown" categories from visualization

## 2. Movies vs TV Shows Distribution

* Compared number of Movies and TV Shows
* Visualized using pie chart

## 3. Top Countries Producing Netflix Content

* Analyzed country-wise content production
* Created horizontal bar chart for better readability

## 4. Ratings Analysis

* Identified most common Netflix ratings
* Visualized rating distribution

## 5. Release Year Analysis

* Analyzed content release trends over years
* Visualized using histogram

## 6. Movie Duration Analysis

* Extracted movie duration in minutes
* Analyzed duration distribution

## 7. Yearly Additions to Netflix

* Converted date columns to datetime format
* Analyzed yearly content additions

---

# Visualizations Included

* Movies vs TV Shows Pie Chart
* Country-wise Content Distribution
* Ratings Analysis Chart
* Release Year Histogram
* Movie Duration Histogram
* Netflix Yearly Additions Trend

---

# Sample Insights

* Movies dominate Netflix content compared to TV Shows.
* United States produces the highest amount of Netflix content.
* TV-MA is one of the most common content ratings.
* Netflix content additions increased significantly after 2015.

---

# Screenshots

## Content Distribution

Add screenshot here:

```bash
screenshots/content_distribution.png
```

## Country Analysis

Add screenshot here:

```bash
screenshots/country_chart.png
```

## Ratings Analysis

Add screenshot here:

```bash
screenshots/ratings_chart.png
```

## Release Year Analysis

Add screenshot here:

```bash
screenshots/release_year_chart.png
```

---

# Future Improvements

* Add Genre Analysis
* Build Interactive Dashboard using Streamlit
* Create Recommendation System
* Add NLP-based content analysis
* Deploy project online

---

# Learning Outcomes

Through this project, I revised and practiced:

* Pandas fundamentals
* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* Feature engineering
* GitHub project structuring

---

# Author

Swarada

---



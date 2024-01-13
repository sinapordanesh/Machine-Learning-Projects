# Project: Netflix Viewership and IMDb Rating Prediction

<div style="text-align: center;">
    <img src="./files/nf.png" alt="phase1" width="800"/>
</div>

## Overview
This project utilizes data science and machine learning techniques to analyze and predict Netflix viewership and IMDb ratings. The primary dataset, released by Netflix, contains around 18,000 movie titles with their viewing hours, enriched with additional data from the OMDB API.

## Data
| Name         | Description             |
|--------------|-------------------------|
|What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.xlsx| Original Netflix data from [here](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report) |
| What_We_Watched_A_Netflix_Engagement_Report_2023Jan-Jun.csv  | Original data in CSV |
| data.csv  | Title sanetized version of the original data  |
| raw_enriched_data.csv  | OMDB API enriched data without any data analyziz    |
| clean_enriched_data.csv  | Enriched dat after all data analyzing steps      |
| training_data.csv  | Final dataset for training machine learning models (All numerics)      |


## Data Analysis Notebooks
- `data_analyziz_1.ipynb`: Initial data sanetization before API enriching. Cleaning titles for better database search.
- `data_analyziz_2.ipynb`: This notebook includes the initial data cleaning processes, such as removing season numbers from titles, cleaning and formatting the dataset, and preparing it for enrichment.
- `data_analyziz_3.ipynb`: This notebook continues the data cleaning process post-enrichment, handles null values, and performs feature extraction, including binary encoding for genres, languages, and countries, as well as one-hot encoding for the type of content.


## Feature Engineering and Model Training
- `model_training_hours.ipynb`: Focuses on the feature engineering and model training for predicting viewing hours. It includes correlation analysis, feature importance from models, univariate feature selection, and recursive feature elimination.
- `model_training_imdb.ipynb`:  Similar to the previous notebook but dedicated to predicting IMDb ratings. It shares methods used in feature selection and importance analysis.


## Models Employed
- RandomForestRegressor
- LinearRegression
- GradientBoostingRegressor
- Polynomial Regression

## Final Dataset Columns
After data preprocessing and feature engineering, the final dataset contains columns that describe whether the title is available globally, the genre in a binary-encoded format, the language of the title also binary-encoded, and the country of origin. Runtime is categorized into five different lengths, and the type of content is encoded as movie or series. The total number of seasons is also included for series.

## Conclusions
The project's machine learning models targeted to predicting viewing hours and IMDb ratings, but after furthure EDA, no meaningful relation ships were found between two targeted features and other dataset properties. We riched the maximum 30% accuracy for predecting viewing hours and 50% for IMDB rating, which are lower than minimum standard 85%. However, more data and machine learning could be applied for deeper understanding of the dataset and any possible machine learning approaches.

## Notebooks Documentation
Each notebook is annotated with markdown cells and comments to guide the user through the data processing and machine learning procedures, ensuring clarity and reproducibility.

For detailed procedures and explanations, please refer to the individual notebooks within the repository.

---


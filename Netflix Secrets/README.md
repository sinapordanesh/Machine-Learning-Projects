# Project: Netflix Viewership and IMDb Rating Prediction

## Overview
This project utilizes data science and machine learning techniques to analyze and predict Netflix viewership and IMDb ratings. The primary dataset, released by Netflix, contains around 18,000 movie titles with their viewing hours, enriched with additional data from the OMDB API.

## Data Analysis Notebooks
- `data_analyziz_2.ipynb`: Cleans and prepares Netflix's initial dataset for enrichment.
- `data_analyziz_3.ipynb`: Further processes the enriched dataset and extracts features for modeling.

## Feature Engineering and Model Training
- `model_training_hours.ipynb`: Engages in feature engineering and model training to predict viewing hours.
- `model_training_imdb.ipynb`: Applies similar techniques to predict IMDb ratings.

## Models Employed
- RandomForestRegressor
- LinearRegression
- GradientBoostingRegressor
- Polynomial Regression

## Final Features
The refined dataset includes global availability, binary-encoded genres, languages, and countries, categorized runtime, content type encoding, and total seasons for series.

## Conclusions
The project's machine learning models are capable of predicting viewing hours and IMDb ratings, demonstrating the effectiveness of the selected features and the modeling approaches.

## Notebooks Documentation
Each notebook is annotated with markdown cells and comments to guide the user through the data processing and machine learning procedures, ensuring clarity and reproducibility.

For detailed procedures and explanations, please refer to the individual notebooks within the repository.

---

**Note**: This README is formatted in markdown for consistency and readability across platforms like GitHub and Jupyter Notebook environments.

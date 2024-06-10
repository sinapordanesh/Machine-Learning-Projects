# SpaceX Fellows

![Project Image](./spacex_fellows.webp)

## Project Description

In this capstone project, we aim to predict whether the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches at a cost of \$62 million, significantly lower than other providers that charge upwards of $165 million. Much of the cost savings are due to SpaceX's ability to reuse the first stage. By predicting the success of the first stage landing, we can estimate the cost of a launch. This information is valuable for alternative companies bidding against SpaceX for rocket launches.

## Learning Objectives

- Develop Python code to manipulate data in a Pandas data frame
- Convert a JSON file into a Pandas data frame
- Create a Jupyter notebook and share it using GitHub
- Utilize data science methodologies to define and formulate a real-world business problem
- Use data analysis tools to load, clean, and analyze a dataset to uncover insights

## Repository Structure

```
SpaceX-Fellows/
├── Data
│   ├── Spacex.csv
│   ├── dataset_part_1.csv
│   ├── dataset_part_2.csv
│   ├── dataset_part_3.csv
│   ├── my_data1.db
│   ├── spacex_launch_dash.csv
│   └── spacex_web_scraped.csv
├── Notebooks
│   ├── 1.1_spacex-data-collection-api.ipynb
│   ├── 1.2_spacex-Data wrangling.ipynb
│   ├── 1.3_webscraping.ipynb
│   ├── 2.1_eda_sql_sqllite.ipynb
│   ├── 2.2_eda_dataviz.ipynb
│   ├── 3.1._Folium_launch_site_location.ipynb
│   └── 4.1_Machine Learning Prediction.ipynb
├── README.md
├── Scripts
│   ├── requirements.txt
│   └── spacex_dash_app.py
└── spacex_fellows.webp
```


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sinapordanesh/Machine-Learning-Projects.git
    cd SpaceX-Fellows
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Data Processing

The data is sourced from SpaceX's API and contains information about various Falcon 9 launches. The data_processing.py script processes the JSON data into a clean Pandas DataFrame. The following steps are performed:
- Loading data from JSON
- Data cleaning and preprocessing
- Saving the processed data to a CSV file

## Model Development

The goal is to build a machine learning model to predict the landing outcome of the Falcon 9 first stage. The 4.1_Machine Learning Prediction.ipynb notebook details the steps taken:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning

## Results and Insights

The analysis revealed key factors influencing the success of the Falcon 9 first stage landing. The final model achieved a high accuracy rate, demonstrating the potential for predicting landing outcomes accurately. The insights gained can aid in strategic decision-making for competitive bidding against SpaceX.

## Contribution Guidelines

We welcome contributions to enhance this project. Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

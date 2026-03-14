# House Price Prediction – Data Analysis & Machine Learning

## Project Overview

This project analyzes residential housing data and builds predictive models to estimate house sale prices based on various structural and neighborhood features.

The project follows a complete data science workflow including:

- Business understanding
- Data auditing
- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model development
- Model evaluation

The objective is to identify the most important factors influencing house prices and develop a predictive model capable of estimating property values accurately.

---

## Dataset

This project uses the **House Prices – Advanced Regression Techniques** dataset from Kaggle.

The dataset contains:

- **1460 observations**
- **79 explanatory variables**
- **Target variable:** `SalePrice`

Features describe different aspects of residential homes including:

- Structural attributes (number of rooms,number of columns):(1460, 81)
- Property quality
- Basement features
- Garage information
- Neighborhood location



### Dataset Setup

Download the dataset from https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

## Project Structure
House-Prices-Dataset/

data/
raw/
processed/

notebooks/
01_business_understanding.ipynb
02_data_audit.ipynb
03_data_cleaning.ipynb
04_eda_analysis.ipynb
05_feature_engineering.ipynb
06_modeling.ipynb
07_model_evaluation.ipynb

src/
utils.py

README.md



Each notebook represents a stage of the data science workflow.

---

## Workflow

### 1. Business Understanding

Defined the project objective and analytical approach for predicting house prices using structured housing data.

The main goal is to analyze housing features and develop a machine learning model capable of estimating property prices accurately.

---

### 2. Data Audit

The dataset was initially inspected to understand its structure and quality.

Key checks performed:

- Dataset dimensions
- Feature data types
- Missing value analysis
- Basic statistical summaries

This step helped identify potential issues in the dataset before further processing.

---

### 3. Data Cleaning

Data cleaning steps included:

- Handling missing values across numerical and categorical features
- Filling numerical values using the **median**
- Filling categorical values with `"None"` where missing values represent absence of a feature
- Verifying that no missing values remain in the dataset
- Applying **log transformation to the target variable (`SalePrice`)** to reduce skewness

After cleaning, the dataset was saved as a processed dataset for further analysis.

---

### 4. Exploratory Data Analysis (EDA)

EDA was performed to explore relationships between features and the target variable.

The analysis included:

- Distribution analysis of `SalePrice`
- Numerical feature distributions
- Categorical feature analysis
- Correlation analysis
- Outlier detection

Important visualizations used:

- SalePrice distribution plot
- Correlation heatmap
- SalePrice vs Overall Quality
- SalePrice vs Living Area
- SalePrice by Neighborhood

---

## Key Insights from EDA

Major findings from exploratory analysis include:

- **OverallQual** (overall house quality) is the strongest predictor of house price.
- Larger living areas (**GrLivArea**) significantly increase property value.
- Basement size (**TotalBsmtSF**) contributes to house pricing.
- Garage capacity (**GarageCars**) influences property prices.
- Neighborhood location significantly impacts house values.

These insights guided the feature engineering stage.

---

## Feature Engineering

Several new features were created to improve model performance and capture more meaningful information from the data.

Engineered features include:

- **TotalSF**  
  Total square footage combining basement and floor areas.

- **HouseAge**  
  Age of the property calculated from the construction year.

- **RemodelAge**  
  Years since the house was last remodeled.

- **TotalBathrooms**  
  Combined metric including full and half bathrooms.

- **TotalPorchSF**  
  Total porch area derived from multiple porch-related features.

These features provide richer representations of house characteristics for machine learning models.

---

## Models Used

Multiple regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor

Categorical variables were encoded using **one-hot encoding** before model training.

The dataset was split into training and testing sets using an **80/20 split**.

---

## Model Evaluation

Model performance was evaluated using the following metrics:

- **Root Mean Squared Error (RMSE)**
- **R² Score**

Additional evaluation methods included:

- Residual analysis
- Actual vs predicted price visualization
- Feature importance analysis

---

## Final Model

Among the tested models, **Random Forest Regressor** achieved the best predictive performance.

Reasons for selecting Random Forest:

- Captures nonlinear relationships between features
- Handles interactions between variables effectively
- Provides useful feature importance insights

The final model demonstrates strong capability in predicting housing prices based on the available features.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## How to Run the Project

1. Clone the repository
        git clone https://github.com/VishnuVardhanKasireddy/data-analysis-portfolio/tree/main/House-Prices-Dataset


2. Install required dependencies
    pip install -r requirements.txt


3. Download the dataset from Kaggle

4. Place the dataset files in:data

5. Run the notebooks in the following order:


01_business_understanding.ipynb
02_data_audit.ipynb
03_data_cleaning.ipynb
04_eda_analysis.ipynb
05_feature_engineering.ipynb
06_modeling.ipynb
07_model_evaluation.ipynb


---

## Project Conclusion

This project demonstrates a complete data science workflow from raw data analysis to predictive modeling.

Key findings from the analysis include:

- Property quality and living area strongly influence house prices.
- Basement size and garage capacity also impact property valuation.
- Neighborhood location plays a major role in determining house prices.

The final Random Forest model effectively captures these relationships and provides accurate price predictions.

---

## Author

**Vishnu Vardhan Kasireddy**

Data Analysis & Machine Learning Portfolio Project


# Car-Price-Predictor
![alt text](https://github.com/shrutimistry01/Car-Price-Predictor/blob/master/readme-resource/car-1.png)
## Project Overview
• Created a machine learning model that **estimates price of a car based on the features like mileage, engine,year etc.**<br/>

## How will this project help?
• This project **helps a car seller or buyer to negotiate the price of the car for an old or a new car**

## Resources Used
• Packages: **pandas, numpy, sklearn, matplotlib, seaborn,flask**<br/>
• Dataset from Kaggle

## Exploratory Data Analysis (EDA) and Data Cleaning
![alt text](https://github.com/shrutimistry01/Car-Price-Predictor/blob/master/readme-resource/graph-year.png)
![alt text](https://github.com/shrutimistry01/Car-Price-Predictor/blob/master/readme-resource/feat-imps.png)

• **Removed unwanted columns**: 'torque,name'<br/
• **Plotted bargraphs and countplots** for numerical and categorical features respectively for EDA<br/>
• **Numerical Features** (mileage,engine,max_power): **Replaced NaN or -1 values with mode or meadian based on their distribution and removed unwanted alphabet/special characters to convert into numerical value**<br/>
• **Categorical Features: Replaced NaN or -1 values **<br/>


## Feature Engineering
• **Creating new features** from existing features e.g. **name_of_company from model_name**<br/>
• Trimming columns i.e. **Trimming features having more than 10 categories to reduce the dimensionality**<br/>
• Feature Selection using ** correlation matrix**<br/>
• Feature Scaling using **StandardScalar**


## Model Prediction
![alt text](https://github.com/shrutimistry01/Car-Price-Predictor/blob/master/readme-resource/result.png)

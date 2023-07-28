# Heritage Housing Issues


The objective of this project is to utilize Data Analytics and Machine Learning techniques to preprocess and refine data for an ML Model. The model aims to predict the value of houses in Ames, Iowa while also providing visual representations of the crucial features taken into account for accurate predictions.

The live project is found here.

Using the **CRISP-DM** methodology, I will outline the steps involved in accomplishing this project.

## CONTENTS

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and Validation](#hypothesis-and-validation)
- [Rationale to map the business requirements to the Data Visualizations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





## Business Requirements

This project showcases the utilization of publicly available datasets to develop effective Machine Learning tools for market analysis, enabling informed decision-making.

Luke Van Holten, a good friend of mine who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, has requested to help him in maximising the sales price for the inherited properties.

Although my friend has an excellent understanding of property prices in his own state and residential area, he fears that basing his estimates for property worth on his current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where he comes from might not be the same in Ames, Iowa. He found a public dataset with house prices for Ames, Iowa, and provided me with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from his four inherited houses and any other house in Ames, Iowa.


## Hypothesis and how to validate?
* 1 -  We can predict the sales price for any house in Ames iowa. 
    * By analysing the database records of the real state transactions made in Ames, state of Iowa, we can predict a sales price for a particular house

* 2 - Some house attributes will affect the price more than others.
    * Size of the ground floor, living area, the basement and garage affect and help determine prices, by analysing historic information from the dataset we will find a guide to fit a price range for our customer's properties.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation Study
    * As a client I want to inspect the data related to the house records, so that I can dicscover how the house attributes correlate with the sale price.
    * As a client I want to conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price, so that I can discover how the house attributes correlate sith the sale price.
    * As a client I want to plot the main variables against Sale Price to visualize insights, so that I can discover how the house attributes correlate sith the sale price.

* **Business Requirements 2:** Sales Price Prediction
    * As a client I want to predict the sale price for a given house. We want to build a ML model, so that the client can predict the house sale price from her 4 inherited houses, and any other house in Ames, Iowa.


To achieve this objective, we will develop a ML system capable of accurately predicting the combined sales price of the four inherited houses. This will be accomplished through the implementation of either conventional ML techniques or Neural Networks, which will effectively capture the relationships between the features and the target variable.

As per our agreement with the client, a minimum R2 score of 0.75 is expected on both the train set and the test set, ensuring the reliability and accuracy of the predictions.

The data will be thoroughly explained and visualized using a dashboard, eliminating the need for an API in this project.


## ML Business Case
* The goal is to develop a Machine Learning (ML) model that can predict and illustrate the sales prices of houses, specifically focusing on a set of four inherited houses and other properties within the vicinity of Ames.
* Given that the Sale Price of houses is a continuous variable, a Supervised Regressor Model is deemed appropriate for this prediction task.
* Ultimately, we aim to empower our client to uncover the relationships between different house attributes and the corresponding sale prices.


## Dashboard Design

* The dashboard was created using Streamlit and is made up of 5 pages.

### Page 1: Project Summary

* Project Terms and Jargons
* Project Dataset
* Business Requirements

### Page 2: Sales Price Study

* State business requirement 1
* Checkbox: data inspection on dataset
* Display the most correlated variables to sale price
* Conclusions from correlation study
* Checkbox: scatterplots of correlated variables against sell price

### Page 3: Predict House Price

* State business requirement 2
* Inherited houses price prediction
* House price predictor

### Page 4: Project Hypothesis and Validations

Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:

* Size, overall quality and year of construction affect the final sale price, with larger houses with better quality and built more recently having a higher final sale price.
    * Correct. The correlation study at SalesPriceStudy Notebook supports that.

### Page 5: ML Sale Price Prediction

* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

## Unfixed Bugs

* No unfixed bugs found.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Python | Main language
* Numpy | Manage data
* Pandas | Profile Report
* Pandas-profiling | Feature analysis
* Ppscore | Correlation analysis
* Scikit Learn | ML Pipelines
* Matplot & Seaborn | Correlation study plots
* Feature-engine | Feature engineering
* Streamlit | Dashboard creation

## Credits 

* The dataset of the housing market is taken from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).

* The Churnometer project was continuously referenced throughout the building of this project.

* The initial repository and part of the README.md file were provided by CodeInstitute.


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_clean_data, load_pkl_file
from src.evaluate_regression import regression_performance
from src.evaluate_regression import regression_evaluation_plots


def page_modelling_body():

    # load sale price pipeline files
    ver = 'v1'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"
    sale_price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    feat_importance = pd.read_csv(f"{path}/feature_importance.csv")
    feat_importance_plot = plt.imread(f"{path}/feature_importance.png")
    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv")
    y_test = pd.read_csv(f"{path}/y_test.csv")

    st.write("### ML Pipeline: Predict Sale Price")
    # display pipeline training summary conclusions
    st.info(
        f"* A Regressor model was chosen to predict sale price \n"
        f"* Feature selection performed slightly better than PCA. "
        f" Therefore, the best pipeline to use will be that "
        f"of feature selection.\n"
        f"* Feature selection achieved an R2 Score: 0.97 on the train set and "
        f"an R2 Score: 0.78 on the test set.\n"
        f"* The client requirement is an R2 Score of 0.75\n"
    )
    st.write("---")

    # show pipeline
    st.write("### ML pipeline")
    st.write(sale_price_pipe)
    st.write("---")

    # show best features
    st.write("### The features the model was trained on and their importance:")

    features = feat_importance['Feature']
    st.write(features)
    st.image(feat_importance_plot)
    st.write("---")

    # evaluate performance on train and test set
    st.write("### Pipeline Performance")
    regression_performance(X_train, y_train, X_test, y_test, sale_price_pipe)
    st.write("---")

import streamlit as st
import pandas as pd
from src.data_management import load_clean_data, load_pkl_file
from src.predictive_analysis_ui import predict_sale_price


def page_predict_house_price_body():

    # load predict house price files
    ver = 'v1'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"

    price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    price_features = (pd.read_csv(f"{path}/X_train.csv")
                      .columns
                      .to_list()
                      )
    feature_importance = list(pd.read_csv(
        f"{path}/feature_importance.csv")['Feature'])

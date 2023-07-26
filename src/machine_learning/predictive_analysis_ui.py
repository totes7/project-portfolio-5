import streamlit as st


def predict_sale_price(X_live, features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(features)

    # predict
    sale_price_prediction = pipeline.predict(X_live_sale_price)

    return sale_price_prediction

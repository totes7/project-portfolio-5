import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We have the ability to forecast the sales price of any house in Ames, Iowa. \n\n"
        f" By thoroughly examining the real estate transaction records in the area, "
        f" we can accurately predict the selling price for a specific house. \n\n"
        f"* Certain attributes of the house hold more influence over the price than others. \n\n"
        f" Factors such as the size of the ground floor, living area, basement, "
        f"and garage play a significant role in determining the property's value. "
        f"Through careful analysis of historical data from the dataset, "
        f"we can establish a reliable price range to assist our customers "
        f"in pricing their properties appropriately. "
    )

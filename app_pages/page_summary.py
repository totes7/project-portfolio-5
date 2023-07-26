import streamlit as st


def page_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* An **Attribute** refers to the individual characteristics or"
        f" properties that describe the house.\n "
        f"* A **Correlation** measures the statistical relationship "
        f" between two variables.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset is sourced from "
        f"**[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)**.\n"
        f"* The dataset has almost 1.5 thousand rows and represents housing "
        f"records from Ames, Iowa, "
        f"indicating house profile (Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck, Year Built) and its "
        f"respective sale price for houses built between 1872 and 2010.")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how house attributes correlate with the sale price.\n"
        f"  Therefore, the client expects data visualizations of the correlated variables against the sale price.\n"
        f"* 2 - The client is interested in predicting the house sales price from his four inherited houses, "
        f"and any other house in Ames, Iowa."
    )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/totes7/project-portfolio-5/blob/main/README.md).")

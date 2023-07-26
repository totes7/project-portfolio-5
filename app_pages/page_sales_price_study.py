import streamlit as st

from src.data_management import load_house_prices_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sales_price_study_body():

    # load data
    df = load_house_prices_data()

    # hard copied from sale price study notebook
    vars_to_study = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### House Sale Price Study")
    st.info(
        f"* The client is interested in discovering how the house attributes "
        f"correlate with the sale price.\n"
        f"* Therefore, the client expects data visualizations of the "
        f"correlated variables against the sale price."
    )

    # inspect data
    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"* The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "Sale Price Study" notebook - "Conclusions and Next Steps" section
    st.info(
        f"#### The correlations indications and plots interpretation converge.\n"
        f"* The correlation study isolated the "
        f" following variables:\n"
        f"* 1stFlrSF: First Floor square feet\n"
        f"* GarageArea: Size of garage in square feet\n"
        f"* GrLivArea: Above grade (ground) living area square feet\n"
        f"* OverallQual: Rates the overall condition of the house\n"
        f"* TotalBsmtSF: Total square feet of basement area\n"
        f"* YearBuilt: Original construction date\n\n"
        f"* Based on the correlation analysis, it is evident that "
        f"the size of the ground floor living area, basement area, "
        f"and garage area significantly influence the house price. \n"
        f"Furthermore, the year of construction and the overall quality "
        f"of materials and finishes in the house also play a crucial role "
        f"in determining the house price.\n"
        f"* The plotted data confirms the strong correlation between the "
        f"isolated variables in the correlation study, suggesting their "
        f"potential as powerful predictors for the sale price."
    )

    # Code copied from "Sale Price Study" notebook
    # "EDA on the Correlated Variable List" section
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable correlation to Sale Price"):
        variable_correlation_to_sale_price(df_eda, vars_to_study)

def variable_correlation_to_sale_price(df_eda, vars_to_study):
    # function created using "Sale Price Study" notebook
    # "Variables Distribution by Sale Price" section
    target_var = 'SalePrice'
    for col in vars_to_study:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")

def plot_numerical(df, col, target_var):
    # function created using "Sale Price Study" notebook
    # "Variables Distribution by Sale Price" section
    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()

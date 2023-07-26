import streamlit as st

from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sales_price_study import page_sales_price_study_body


# Create an instance of the app
app = MultiPage(app_name="Heritage Housing")

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Sales Price Study", page_sales_price_study_body)

app.run()  # Run the app

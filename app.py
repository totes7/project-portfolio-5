import streamlit as st

from app_pages.multipage import MultiPage


# Create an instance of the app
app = MultiPage(app_name="Heritage Housing")

app.run()  # Run the app

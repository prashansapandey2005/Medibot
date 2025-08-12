import os
import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv, find_dotenv

# Load environment variables for API keys
load_dotenv(find_dotenv())
import home, creater, about, xai_SHAP

# Set page config as the VERY FIRST Streamlit command
st.set_page_config(page_title="MediBot AI")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            st.image("name.jpeg", width=300)
            st.image("logo.png", width=200)

            medibot = option_menu(
                menu_title='Explore ',
                options=['Home', 'Creator', 'About', 'Diagonstic Assistant'],
                icons=['house-fill', 'person-circle', 'info-circle-fill', 'activity'],
                menu_icon='three-lines-fill',
                default_index=3,  # Set default_index to 3 for "Diagonstic Assistant"
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if medibot == "Home":
            home.main()
        
        if medibot == "Creator":
            creater.medibot()
        if medibot == "About":
            about.medibot()

# Create an instance of MultiApp and run it
app = MultiApp()
app.run()
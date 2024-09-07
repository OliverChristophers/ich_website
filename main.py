import streamlit as st
from utils.about_us import about_us
from utils.who_are_we import who_are_we
from utils.scraper_and_data import scraper_and_data
from utils.modelling_example import modelling_example
from utils.references import references


if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

if st.session_state.page == 'main_page':
    selection = 'About us'

    st.sidebar.title('Navigation')
    options = ['About us', 'Who are we?', 'Scraper and data', 'Modelling example','References']
    selection = st.sidebar.radio("Go to", options,)
    if selection == 'About us':
        about_us()
    elif selection == 'Who are we?':
        who_are_we()
    elif selection == 'Scraper and data':
        scraper_and_data()
    elif selection == 'Modelling example':
        modelling_example()
    else:
        references()
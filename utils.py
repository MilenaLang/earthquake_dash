import sys
import streamlit as st
from PIL import Image
import pandas as pd


def set_sidebar():
    """
    This function creates a sidebar with some explanatory and additional information
    :return: Sidebar
    """
    st.sidebar.title("Earthquake Dashboard")

    st.sidebar.write("This earthquake dashboard is designed to analyze and visualize all earthquakes "
                     "occurring worldwide since 1800. It provides information and maps on "
                     "magnitudes, deaths, and damages.")

    # add image
    image = Image.open('data/erdbeben.jpg')
    st.sidebar.image(image, caption="Earthquake in Taiwan (derived from https://rp-online.de/panorama/ausland/taiwan-erdbeben-der-staerke-6-4-reisst-menschen-aus-dem-schlaf_bid-18908485)")

    st.sidebar.info(
            """
            This app is developed by Milena Lang (last updated 10.10.2022).
            """
        )


def read_data():
    """
    THis function reads in the earthquake csv file and returns
     a pandas dataframe with reformatted lat/lon-columns
    :return: data pandas DF
    """
    # read data
    try:
        data = pd.read_csv(
            "/Users/milenalang/Documents/Studium/Master/advanced_geoscripting/earthquake_dash/data/earthquakes1800_2021.csv")

        # rename the columns for streamlit and delete the ones missing coordinates
        data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'}, inplace=True)
        data = data[data['longitude'].notna()]
        data = data[data['latitude'].notna()]
    except Exception:
        st.write("Could not open file")
        sys.exit()
    return data

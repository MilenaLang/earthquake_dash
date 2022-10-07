#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""An earthquake dashboard - Utility functions"""

import sys
import streamlit as st
from PIL import Image
import pandas as pd

def set_sidebar():
    """
    This function creates a sidebar with some explanatory and additional information
    :return: Sidebar
    """
    # set sidebar title
    with st.sidebar:
        st.title("Earthquake Dashboard")

        # provide additional information
        st.write("This earthquake dashboard is designed to analyze and visualize all earthquakes "
                         "occurring worldwide since 1800. It provides information and maps on "
                         "magnitudes, deaths, and damages.")

        # add earthqauke image
        image = Image.open('data/erdbeben.jpg')
        st.image(image, caption="Earthquake in Taiwan (derived from"
                                        " https://rp-online.de/panorama/ausland/taiwan-erdbeben-"
                                        "der-staerke-6-4-reisst-menschen-aus-dem-schlaf_bid-18908485)")

        # add developer information
        st.info(
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
    try:
        url = "data/earthquakes1800_2021.csv"
        data = pd.read_csv(url)
        # rename the columns for streamlit and delete the ones missing coordinates
        data.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'}, inplace=True)
        data = data[data['longitude'].notna()]
        data = data[data['latitude'].notna()]
    except Exception:
        st.error("Could not open file")
        sys.exit()
    return data

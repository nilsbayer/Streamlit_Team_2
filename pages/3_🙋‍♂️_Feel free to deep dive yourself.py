import streamlit as st
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import pydeck as pdk

@st.experimental_singleton
def load_data():
    data = pd.read_csv('./Vending_machine_Data.csv')
    data['date'] = pd.to_datetime(data["date"])
    data.set_index('date', inplace=True)

    return data

data = load_data()

# SIDEBAR CONTENT

start = st.sidebar.date_input(
    "Starting date",
    datetime(2022, 1, 1))

# start = np.datetime64(start)

end = st.sidebar.date_input(
    "Ending date",
    datetime(2022, 8, 31))

# end = np.datetime64(start)

st.sidebar.markdown("##### Select dates between 01.01.2022 and 31.08.2022.")

data = data[start : end]


# START OF SITE'S CONTENT

col1, col2 = st.columns(2)

with col1:
    pass

with col2:
    pass

fig = px.pie(
    data, values='TransTotal', names='Category',
    hole=0.5
    )
st.plotly_chart(fig, use_container_width=True)



midpoint = (np.average(data["Latitude"]), np.average(data["Longitude"]))

st.pydeck_chart(pdk.Deck(
    map_style="road",
    initial_view_state=pdk.ViewState(
        latitude=midpoint[0],
        longitude=midpoint[1],
        zoom=8.35,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=data[["Longitude", "Latitude"]],
           get_position=['Longitude', 'Latitude'],
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        )
        # pdk.Layer(
        #     'ScatterplotLayer',
        #     data=data[["Longitude", "Latitude"]],
        #     get_position='[Longitude, Latitude]',
        #     get_color='[200, 30, 0, 160]',
        #     get_radius=200,
        # ),
    ],
))
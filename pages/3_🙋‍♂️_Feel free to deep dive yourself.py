import streamlit as st
from datetime import datetime
from datetime import date
import numpy as np
import pandas as pd
import plotly.express as px
import pydeck as pdk
from streamlit.components.v1 import html


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

if start < date(2022, 1, 1):
    st.sidebar.error("Choose a starting date from 01.01.2022")

# start = np.datetime64(start)

end = st.sidebar.date_input(
    "Ending date",
    datetime(2022, 8, 31))

if end > date(2022, 8, 31):
    st.sidebar.error("Choose an ending date until 31.08.2022")

# end = np.datetime64(start)

st.sidebar.markdown("##### Select dates between 01.01.2022 and 31.08.2022.")

data = data[start : end]


# START OF SITE'S CONTENT

html('''\
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap" rel="stylesheet">
<style>
    *{
        font-family:'Source Sans Pro', sans-serif;
    }
    span{
        font-size:4rem;
    }
    #sp1{
        color:#D54C34;
    }
    #sp2{
        color:#00CC96;
    }
    #sp3{
        color:#636EFA;
    }
    small{
        font-size:1.2rem;
        animation: color 2s alternate-reverse infinite;
    }
    @keyframes color {
        from {
            color:black;
        }
        to {
            color: #0078D7;
        }
    }
    div{
        animation: move 1.2s ease-in-out alternate-reverse infinite;
    }
    @keyframes move {
        to {
            transform: translateX(10px);
        }
    }

</style>
<span id="sp1">EX</span><span  id="sp2">PL</span><span id="sp3">ORE</span>
<div><small>⬅️ Select a time frame and take a look at the item sales!</small></div>
''')

st.markdown("## Distribution of sold categories")

fig = px.pie(
    data, values='TransTotal', names='Category',
    hole=0.5
    )
st.plotly_chart(fig, use_container_width=True)



st.markdown("## Comparing locations on the map")

midpoint = (np.average(data["Longitude"]), np.average(data["Latitude"]))

st.pydeck_chart(pdk.Deck(
    map_style="road",
    initial_view_state=pdk.ViewState(
        latitude=midpoint[0],
        longitude=midpoint[1],
        zoom=10, 
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=data[["Latitude", "Longitude"]],
           get_position=['Latitude', 'Longitude'],
           radius=600,
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

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Best sold products")
    st.write(data["Product"].value_counts().head())

with col2:
    st.markdown("#### Revenue per location")
    st.write(data.groupby("Location")["LineTotal"].sum().sort_values(ascending=False))
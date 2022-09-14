import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image

st.title('Hackathon Group 2')
st.header('Vending machine sales in central New Jersey')
st.write('''The following application is for visualizing data from vending machines in specific locations
in central New Jersey.''')

data = pd.read_csv('./vending_machine_sales.csv')
data.dropna(inplace=True)


image = Image.open('vending_machines_picture.PNG')

st.image(image, caption='Data info')








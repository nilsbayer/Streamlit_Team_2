import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit.components.v1 import html


# st.title('Hackathon Group 2')
html("""\
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap" rel="stylesheet">
<h1 style="color:grey;font-family:'Source Sans Pro', sans-serif;font-size:3rem;margin:0;padding:0;box-sizing:border-box">Hackathon Group 2</h1>
""")

st.header('Vending machine sales in central New Jersey')
st.write('''The following application is for visualizing and analyzing data from vending machines in four
specific locations in central New Jersey in the time period 2022.01.01 to 2022.08.31.''')
st.write('The following will be analysed:')
st.write('What product and category sells the most.')
st.write('What location sells the most.')
st.write('When are the vending machines selling the most.')

image = Image.open('vending_machines_picture.PNG')

st.image(image, caption='Image 1: Data info')
st.write('''Image 1 shows the columns and all the amount of entries and what kind of type these are. 
Note the dataset is cleaned for null values at this moment.''')
st.write('Status : Represents if the machine data is successfully processed')
st.write('Device ID : Unique electronic identifier ( also called as ePort) for the vending machine. A machine is allocated a unique ePrt * device')
st.write('Location : Indicates location of the vending machine')
st.write('Machine : User-friendly machine name')
st.write('Product : Product vended from the machine')
st.write('Category : Carbonated / Food / Non-carbonated / Water')
st.write('Transaction : Unique identifier for every transaction')
st.write('TransDate : The Date & time of transaction')
st.write('Type : Type of transaction ( Cash / Credit )')
st.write('RCoil : Coil # used to vend the product')
st.write('RPrice : Price of the Product')
st.write('RQty : Quantity sold. This is usually one but machines can be configured to sell more items in a single transaction')
st.write('MCoil : Mapped coil # used to vend the product ( from toucan )')
st.write('MPrice : Mapped price of the Product')
st.write('MQty : Mapped quantity sold. This is usually one but machines can be configured to sell more items in a single transaction')
st.write('LineTotal : Total sale per transaction')
st.write('TransTotal : Represents total of all transactions that will show up on the Credit Card. A user could vend a drink for 3 dollars and a snack for 1.5 dollars making a total of 4.50 dollars')
st.write('Prcd Date : Date when the transaction was processed by SeedLive ( an entity that is used to aggregate all transactions electronically )')
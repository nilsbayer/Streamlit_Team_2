import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.experimental_singleton
def load_data():
    data = pd.read_csv('./vending_machine_sales.csv')
    data.dropna(inplace=True)
    data['date'] = pd.to_datetime(data["TransDate"])
    data.set_index('date', inplace=True)

    return data

data = load_data()

def add_data(data):
    data["best_seller"] = False
    data.loc[data['Product'] == "Coca Cola - Zero Sugar", 'best_seller'] = True
    data.loc[data['Product'] == "Monster Energy Original", 'best_seller'] = True
    data.loc[data['Product'] == "Poland Springs Water", 'best_seller'] = True
    data.loc[data['Product'] == "KitKat - Crisp Wafers", 'best_seller'] = True
    data.loc[data['Product'] == "Sunkist Soda - Orange", 'best_seller'] = True
    data.loc[data['Product'] == "Red Bull - Original", 'best_seller'] = True
    data.loc[data['Product'] == "Coca Cola - Regular", 'best_seller'] = True
    data.loc[data['Product'] == "Wonderful Pistachios - Variety", 'best_seller'] = True
    data.loc[data['Product'] == "CheezIt - Original", 'best_seller'] = True
    data.loc[data['Product'] == "SunChips Multigrain - Harvest Cheddar", 'best_seller'] = True
    data.loc[data['Product'] == "Robert Irvine's - Fit Crunch -  Chocolate Pea", 'best_seller'] = True
    data.loc[data['Product'] == "Snapple Diet Tea - Peach Tea", 'best_seller'] = True
    data.loc[data['Product'] == "Oreo Mini", 'best_seller'] = True
    data.loc[data['Product'] == "SunChips Multigrain - Salsa", 'best_seller'] = True
    data.loc[data['Product'] == "Takis - Hot Chilli Pepper & Lime", 'best_seller'] = True
    data.loc[data['Product'] == "Goldfish Baked - Cheddar", 'best_seller'] = True
    data.loc[data['Product'] == "Snapple Diet Tea - Lemon", 'best_seller'] = True
    data.loc[data['Product'] == "Cheetos - Fleming Hot Crunchy", 'best_seller'] = True
    data.loc[data['Product'] == "Funyuns - Flaming Hot", 'best_seller'] = True
    data.loc[data['Product'] == "Snapple Tea - Raspberry", 'best_seller'] = True

    best_pros = data[data["best_seller"] == True]
    return best_pros

st.title('Analysis')

# PIE CHART

st.markdown("### Visual chart of most bought product category")

fig = px.pie(
    data, values='TransTotal', names='Category',
    hole=0.5
)
# fig.update_layout(title='')

st.plotly_chart(fig, use_container_width=True)

# BEST PRODUCTS

st.markdown("### Visual chart of most bought products by revenue")

best_pros = add_data(data)

fig = px.pie(
    best_pros, values="TransTotal", names="Product", hole = 0.5, width=800, height=520,
)  
# fig.update_layout(title='Visual chart the most revenue-generating products sold')
fig.show()

st.plotly_chart(fig, use_container_width=True)



# SEABORN CHART
st.markdown("### Distribution of sales in the different locations")

plt.figure(figsize=(12,8))
ax = sns.countplot(x="Location", data = data)
plt.title('Distribution of sales per location')
plt.xlabel('Location')
plt.ylabel('Revenue [$]')

for p in ax.patches:
    ax.annotate('${:.1f}'.format(p.get_height()), (p.get_x()+0.1, p.get_height()+50))

st.pyplot(fig.show())

# ANOTHER PLOTLY

st.markdown("### Summary of vending machine sales per location from Jan, 2020 to Aug, 2020, NJ")

fig = px.bar(data, x = data.index, y='TransTotal', color='Location', hover_name='Product')

st.plotly_chart(fig, use_container_width=True)
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Financial Data Analysis",
                   layout="centered",
                   page_icon="image.png")
data = pd.read_csv("./data.csv")
st.subheader("Dataset Preview For Companies in the Nairobi Stock Exchange Market(NSE)")
data["date"] = pd.to_datetime(data["date"], errors="coerce")
data["Month"] = data["date"].dt.month
data["Year"] = data["date"].dt.year
data["price"] = pd.to_numeric(data["price"], errors="coerce")
col1, col2 = st.columns(2)
with col1:
    option=st.checkbox("Select Log Axis")

ticker = st.sidebar.selectbox("Choose a Company",
                             data.ticker.unique())
filtered_data = data[(data.ticker == ticker)]
fig1 = px.bar(data, x="ticker", y="price", color="ticker",
              hover_name="company",
              hover_data=["date", "price"], log_y="option", title="BarChart for Company And Price")
fig1.show()
st.plotly_chart(fig1)
fig = px.line(
    data, x="ticker", y="price", color="ticker",
              hover_name="company",
              hover_data=["date", "price"], log_y="option", title="LineChart for Company And Price")
st.plotly_chart(fig)

import streamlit as st
import pandas as pd

st.title("✅ Test Deployment")

url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
df = pd.read_csv(url)
st.dataframe(df.head())

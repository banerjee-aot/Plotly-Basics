import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard App')
data = px.data.gapminder()
st.table(data.head())
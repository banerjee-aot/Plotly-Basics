### Plotly-Streamlit Env Setup And Run App
## Step 1
```
python -m venv myenv 
```
---
## Step 2
```
.\myenv\Scripts\activate
```
---
## Step 3
```
pip install streamlit plotly
```
---
## Streamlit Code Example
```python
# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard App')
data = px.data.gapminder()
st.table(data.head())
```
---
## Run Web-App
```
streamlit run app.py
```
---
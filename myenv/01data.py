import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Data Visualization App')
data = px.data.gapminder()
st.table(data.head())

selected_year = st.sidebar.slider("Select Year : ", min_value = 1952, max_value = 2007, value = 2007)

selected_population = st.sidebar.slider("Select Population : ", 
                                        min_value = int(data['pop'].min()), 
                                        max_value = int(data['pop'].max()), 
                                        value = (int(data['pop'].min()),int(data['pop'].max())))

st.write('Selected Population :', selected_population)

selected_continent = st.sidebar.selectbox("Select Continent :", data['continent'].unique())


filtered_data = data[(data['year'] == selected_year) & 
                     (data['continent'] == selected_continent) & 
                     (data['pop'] >= selected_population[0]) & 
                     (data['pop'] <= selected_population[1])]


st.table(filtered_data)

fig = px.scatter(filtered_data, x = "gdpPercap", y = "lifeExp" , color = "country",size = "pop", size_max= 80 ,title=f'Life Expectancy vs GDP Per capital {selected_year}', log_x = True)
# fig = px.scatter(data.query('year == @selected_year'), x = "gdpPercap", y = "lifeExp" , color = "country",size = "pop", size_max= 80 ,title=f'Life Expectancy vs GDP Per capital {selected_year}', log_x = True)


st.plotly_chart(fig)

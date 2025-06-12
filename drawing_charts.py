import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Yogesh", "Anuj", "Yuvraj"]
)

# Line Chart
st.header("Line Chart")
st.line_chart(chart_data)

# Bar Chart
st.header("Bar Chart")
st.bar_chart(chart_data)

# Area Chart
st.header("Area Chart")
st.area_chart(chart_data)

# Matplotlib Chart
st.header("Matplotlib Chart")
fig, ax = plt.subplots()
ax.plot([10, 20, 30], [1, 4, 9])
st.pyplot(fig)

# Plotly Chart
st.header("Plotly Chart")
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)

# Altair Chart
st.header("Altair Chart")

df = pd.DataFrame({
    'Name': ['Yogesh', 'Anuj', 'Yuvraj'],
    'Score': [88, 92, 85]
})

chart = alt.Chart(df).mark_bar().encode(
    x='Name',
    y='Score'
)

st.altair_chart(chart, use_container_width=True)


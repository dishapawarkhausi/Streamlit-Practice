import streamlit as st
import pandas as pd

# Static Table
data = pd.DataFrame({
    'Name': ['Yogesh', 'Yuvraj', 'Anuj'],
    'Score': [85, 92, 78]
})
st.header("Static Table")
st.table(data)

# Interactive Table
st.header("Interactive Table")
st.dataframe(data)

# Smart Display
st.header("Smart display")
st.write(data)

# Highlighting Data
st.header("Highlight data")
styled_df = data.style.highlight_max(axis=0)
st.dataframe(styled_df)

# Displaying CSV Data
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here's your data:")
    st.dataframe(df)

# Showing Dictionary / List
st.header("Show Dictionary/List")
my_dict = {"Python": 95, "Java": 90, "C++": 88}
st.write(my_dict)

my_list = ["Apple", "Banana", "Mango"]
st.write(my_list)


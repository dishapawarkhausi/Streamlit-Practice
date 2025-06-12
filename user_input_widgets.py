import streamlit as st
import datetime

# Button
if st.button("Click Me"):
    st.write("You clicked the button!")

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")

# Radio Buttons
option = st.radio("Choose one:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Selectbox
choice = st.selectbox("Pick a fruit", ["Apple", "Banana", "Mango"])
st.write("Your favorite fruit is:", choice)

# Multiselect
multi = st.multiselect("Select multiple fruits", ["Apple", "Banana", "Mango"])
st.write("You selected:", multi)

# Slider
age = st.slider("Select your age", 1, 100, 25)
st.write("Your age is:", age)

# Text Input
name = st.text_input("Enter your name", "Yogesh")
st.write("Hello,", name)

# Number Input
number = st.number_input("Enter a number", min_value=0, max_value=100, value=10)
st.write("You entered:", number)

# Date and Time Input
import datetime

d = st.date_input("Pick a date", datetime.date.today())
t = st.time_input("Pick a time", datetime.time(12, 00))
st.write("Date:", d, "Time:", t)

# File Uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    st.image(uploaded_file)

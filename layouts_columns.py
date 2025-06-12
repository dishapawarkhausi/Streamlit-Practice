import streamlit as st
import time

# Columns – Side-by-side layout
col1, col2 = st.columns(2)

with col1:
    st.write(" 👈This is column 1")
    st.button("Click me!")

with col2:
    st.write(" 👉This is column 2")
    st.slider("Pick a number", 0, 100)

# Expander – Hide/Show on click
with st.expander("Click to see more"):
    st.write("Here is some hidden content.")
    st.image("https://picsum.photos/200")

# Sidebar – Clean up the main page    
st.sidebar.title("Options")
selected = st.sidebar.selectbox("Choose one:", ["Home", "About", "Contact"])
st.write("You selected:", selected)

# Container – Group items together
container = st.container()
container.write("This is inside a container")
container.line_chart([1, 5, 2, 6])

# Empty – Placeholder for future content
placeholder = st.empty()

for i in range(5):
    placeholder.text(f"Loading... {i}")
    time.sleep(1)

placeholder.text("Done!")

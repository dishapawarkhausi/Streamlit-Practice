import streamlit as st
import os

st.set_page_config("Assignment Viewer", layout="centered")
st.title("📘 Assignment Code + Output viewer")
st.markdown("👩‍💻 Created by Disha Pawar")

code_files = [f for f in os.listdir() if f.endswith(".py") and f != "app.py"]

if not code_files:
    st.warning("No .py found in this folder.")
else:
    selected_file = st.selectbox("📂 Select a Python file to view and run:", code_files)

    with open(selected_file, "r", encoding="utf-8") as f:
        code = f.read()

    st.subheader("✅ Output:")
    try:
        exec(code, {'st': st})
    except Exception as e:
        st.error(f"Error while running the code: {e}")



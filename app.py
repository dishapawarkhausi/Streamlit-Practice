import streamlit as st
import os

st.set_page_config(page_title="Assignment Viewer", layout="centered")
st.title("📚 Assignment Code + Output Viewer")
st.markdown("👩‍💻 Created by **Disha Pawar**")

# Get all .py files in current folder (except app.py itself)
code_files = [f for f in os.listdir() if f.endswith(".py") and f != "app.py"]

if not code_files:
    st.warning("No .py files found in this folder.")
else:
    selected_file = st.selectbox("📂 Select a Python file to view and run:", code_files)

    # Display code from selected file
    with open(selected_file, "r") as f:
        code = f.read()

    st.subheader("📄 Code:")
    st.code(code, language="python")

    # Run the code and display the output
    st.subheader("✅ Output:")
    try:
        # Create a safe execution context (can isolate variables if needed)
        exec(code, {'st': st})
    except Exception as e:
        st.error(f"⚠️ Error while running the code: {e}")

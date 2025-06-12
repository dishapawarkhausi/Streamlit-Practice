import streamlit as st

#  Simple Button

if st.button("Say Hello"):
    st.write("Hello, Yogesh 👋")
else:
    st.write("Click the button above.")

# Form with Multiple Inputs
with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Your age", min_value=1, max_value=100)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Welcome, {name}! Age: {int(age)}")

# Login Form with Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")

        if login:
            if username == "Disha" and password == "1234":
                st.session_state.logged_in = True
                st.success("✅ Login successful!")
            else:
                st.error("❌ Invalid credentials")
else:
    st.success("🎉 You are logged in!")
    st.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))


# Feedback Form Example
with st.form("feedback_form"):
    rating = st.slider("Rate your experience (1-10)", 1, 10)
    comments = st.text_area("Any comments?")
    send = st.form_submit_button("Send Feedback")

    if send:
        st.success(f"Thank you for rating us {rating}/10! 😊")
        if comments:
            st.info(f"You said: {comments}")

            
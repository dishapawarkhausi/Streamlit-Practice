import streamlit as st
from PIL import Image

# Display Image
# image = Image.open("your_image.jpg")  # Local file
# st.image(image, caption="My Picture", use_column_width=True)

# Or from a URL:
st.header("Random Image")
st.image("https://picsum.photos/400", caption="Random Image")

# Play Audio
st.header("Audio File")
audio_file = open("harry-potter-theme.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

# Play Video
st.header("Video file")
video_file = open("115977-706323918_tiny.mp4", "rb")
st.video(video_file.read())


# Counter with Session State
# Initialize state variable
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1

st.button("Increase", on_click=increment)
st.write("Count:", st.session_state.count)

# Remember Uploaded Image
import streamlit as st
from PIL import Image

st.title("Upload and View Image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file:
    st.session_state["image"] = uploaded_file  # Save in session

# Check session and show
if "image" in st.session_state:
    img = Image.open(st.session_state["image"])
    st.image(img, caption="Uploaded Image", use_column_width=True)

    
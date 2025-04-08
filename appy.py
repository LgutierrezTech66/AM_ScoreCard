import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(page_title="Carnival Horse Race", layout="wide")

# Load background
background_path = "assets/background.jpg"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_path}');
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load horse images
horse_images = [f"assets/horse{i+1}.png" for i in range(10)]
horse_names = ["Garlic", "Pepper", "Chili", "Cinnamon", "Nutmeg", "Thyme", "Basil", "Oregano", "Saffron", "Clove"]

st.title("🎡 Carnival Horse Racing Game")
st.markdown("🏁 Move your horse by completing tasks! Each horse's position reflects their progress.")

# Inputs for progress
st.sidebar.header("🐎 Horse Progress Input")
progress = {}
for i, name in enumerate(horse_names):
    progress[name] = st.sidebar.slider(f"{name}'s Progress", 0, 100, 0, key=name)

# Display race
track_length = 800  # Pixels
horse_height = 80

st.write("---")
for i, name in enumerate(horse_names):
    col1, col2 = st.columns([1, 9])
    with col1:
        st.write(f"**{name}**")
    with col2:
        percent = progress[name] / 100
        space = int(track_length * percent)

        horse_path = horse_images[i]
        if os.path.exists(horse_path):
            horse_img = Image.open(horse_path).resize((60, 60))
            st.image(horse_img, width=60)
            st.markdown(
                f"<div style='position: relative; left: {space}px; top: -60px;'>"
                f"<img src='data:image/png;base64,{horse_img_to_base64(horse_img)}' width='60'/>"
                "</div>",
                unsafe_allow_html=True
            )

# Helper function to encode images
import base64
from io import BytesIO

def horse_img_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO
import time

# --- SETUP ---
st.set_page_config(page_title="Carnival Horse Race", layout="wide")

# Paths
background_path = "assets/background.jpg"
cheer_sound_path = "assets/cheer.mp3"

# Load background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{background_path}');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Helper functions ---
def load_image_as_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def play_cheer(progress):
    milestones = [50, 75, 100]
    if any(progress == m for m in milestones):
        audio_file = open(cheer_sound_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3', start_time=0)

# --- APP LOGIC ---
horse_names = ["Garlic", "Pepper", "Chili", "Cinnamon", "Nutmeg", "Thyme", "Basil", "Oregano", "Saffron", "Clove"]
horse_images = [f"assets/horse{i+1}.png" for i in range(10)]
horse_base64 = [load_image_as_base64(img) for img in horse_images]

st.title("🎡 Carnival Horse Racing Game")
st.markdown("🏁 Update each horse’s progress and watch them race!")

# Progress Inputs
st.sidebar.header("🐎 Update Horse Progress")
progress = {}
for i, name in enumerate(horse_names):
    progress[name] = st.sidebar.slider(f"{name}'s Progress", 0, 100, 0, step=5, key=name)

# Start Animation
st.write("## 🐴 Race Track")

for i, name in enumerate(horse_names):
    percent = progress[name]
    space = int(percent * 8)  # Scale to pixels
    
    # Play cheering sound at milestones
    play_cheer(percent)

    horse_html = f"""
    <div style="position: relative; height: 80px;">
        <div style="position: absolute; left: {space}px; transition: left 1s ease;">
            <img src="data:image/png;base64,{horse_base64[i]}" width="60"/>
        </div>
    </div>
    """
    st.markdown(f"**{name}**")
    st.markdown(horse_html, unsafe_allow_html=True)

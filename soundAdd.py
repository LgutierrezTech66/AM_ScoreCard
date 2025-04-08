import streamlit as st
from PIL import Image
import time

# Load images and sounds
def load_assets():
    # Load vegetable images
    veg_images = {
        "Garlic": Image.open("assets/garlic.png"),
        "Onion": Image.open("assets/onion.png"),
        # Add other vegetables here
    }
    # Load cheering sound
    cheer_sound = "assets/cheer.mp3"
    return veg_images, cheer_sound

veg_images, cheer_sound = load_assets()

# Initialize session state for progress tracking
if 'progress' not in st.session_state:
    st.session_state.progress = {veg: 0 for veg in veg_images.keys()}

# Function to play sound
def play_sound():
    st.audio(cheer_sound, format='audio/mp3', start_time=0)

# Display progress bars and images
for veg, img in veg_images.items():
    st.image(img, caption=veg, width=100)
    st.progress(st.session_state.progress[veg])

# Update progress and check for milestones
for veg in veg_images.keys():
    new_progress = st.slider(f"Update {veg} progress", 0, 100, st.session_state.progress[veg], 5)
    if new_progress != st.session_state.progress[veg]:
        st.session_state.progress[veg] = new_progress
        if new_progress in [50, 75, 100]:
            play_sound()

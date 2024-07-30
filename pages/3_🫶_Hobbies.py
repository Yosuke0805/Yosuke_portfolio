import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# load profile image
img_profile = Image.open("images/profile_photo.jpg")
with st.sidebar:
    st.image(img_profile, width=200)
# TODO: Upload image on cloud to load by URL
# st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

img_1 = Image.open("images/Cappadocia.jpeg")
img_2 = Image.open("images/snowboading.jpg")
img_3 = Image.open("images/workout.JPG")

st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

with col1:
   st.write("Traveling")
   st.image(img_1)

with col2:
   st.write("Snowboarding")
   st.image(img_2)

with col3:
   st.write("Workout")
   st.image(img_3)


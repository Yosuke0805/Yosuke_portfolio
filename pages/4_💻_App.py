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

st.markdown("[Click here to visit my app for summarizing meeting meniuts from audio file!!](https://summarizemeetingminutesapp-bzha9c2qlxsveh46xmeebm.streamlit.app/)")

st.title("💻 My applications")



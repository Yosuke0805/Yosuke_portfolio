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

st.title("💻 My applications")

st.markdown("**These are the application that I built by myself in my spare time. Let me know what you think and feel free to request any functions!!**")

# summarizing meeting minutes from audio file
st.header("Summarizing meeting minutes from audio file")
description = """
Have you ever thought that you wanted to automate creating meeting minutes especially when you attend international meetings where people speak differenct languages?
Well, this app is for you!!  
All you have to do for taking advantage this app is following two things.
1. Record a meeting.
2. Generate gemini API key and click on the button. You can generate your gemini API key [here](https://aistudio.google.com/app/apikey)

When you open the app, drop down audio file that you record and select the original language that is spoken in meeting and the target language that you want to summarize in and click on the button.
This way, you won't waste your precious time and it is completely free!!
"""
st.markdown(description)
st.markdown("Click below button to visit my app for summarizing meeting meniuts from audio file!!")
url = "https://summarizemeetingminutesapp-bzha9c2qlxsveh46xmeebm.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url}" type="url_app" target="_blank" >Try app</a>
""", unsafe_allow_html=True)




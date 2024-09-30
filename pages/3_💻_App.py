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

# recommending movies
st.header("🎥 Reccomending movies")
st.subheader("Discription")
description_movies = """
Have you ever experienced binge-watching movies and need help deciding what to watch next but were too dull to search for movies??
Here is the app for you!
All you have to do is choose the category and movies that you like, click on the button, and the top 10 recommended movies will be shown.
I am afraid that this app is not personalized to your taste. If you want to get personalized recos, let me know, and I will try to create a personalized recommendation;)
Check it out!
"""
st.markdown(description_movies)
st.markdown("Click below button to visit my app for recommending movies!!")
url_movies = "https://moviesrecommenderapp-by-yosuke.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_movies}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)

# suggesting travel itinerary
st.header("🛫 Suggesting travel itinerary")
st.subheader("Discription")
description_itinerary = """
Since I am huge fun of traveling, I always spend a bunch of time of what to do in my spare time.
Maybe you too??
Well, this app is a time saver to suggest travel itinerary for you!
This will give you a roughly idea of what you can do during travel.
You will need Gemini API key and input it on the sidebar. You can generate your Gemini API key [here](https://aistudio.google.com/app/apikey)
Let me know if you want to customize more then I will modify the app!!
"""
st.markdown(description_itinerary)
st.markdown("Click below button to visit my app for suggesting you an travel itinerary!!")
url_itinerary = "https://why-do-not-travel-somewhere.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_itinerary}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)

# summarizing meeting minutes from audio file
st.header("📋 Summarizing meeting minutes from audio file")
st.subheader("Discription")
description_summary = """
Have you ever thought that you wanted to automate creating meeting minutes especially when you attend international meetings where people speak different languages?
Well, this app is for you!!  
All you have to do to take advantage of this app is follow two things.

1. Record a meeting.
2. Generate Gemini API key and click on the button. You can generate your Gemini API key [here](https://aistudio.google.com/app/apikey)

When you open the app, drop down the audio file that you recorded and select the original language that is spoken in the meeting and the target language that you want to summarize, and click on the button.
This way, you won't waste your precious time and it is completely free!!

"""
st.markdown(description_summary)
st.markdown("Click below button to visit my app for summarizing meeting meniuts from audio file!!")
url_summary = "https://summarizemeetingminutesapp-bzha9c2qlxsveh46xmeebm.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_summary}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)




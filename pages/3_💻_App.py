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

st.markdown("**These are the ML/LLM application that I built by myself in my spare time. Let me know what you think and feel free to request any functions!!**")
st.markdown("※ Apps might need to be rebooted. Don't worry it's just simply pressing the button ;)")

# recommending movies
st.header("🎥 Recommending movies")
st.subheader("Discription")
description_movies = """
Have you ever experienced binge-watching movies and need help deciding what to watch next but were too dull to search for movies?? 
Here is the app for you! 
All you have to do is choose the category and movies that you like, click on the button, and the top 10 recommended movies will be shown. 
I am afraid that this app is not personalized to your taste. 
If you want to get personalized recos, let me know, and I will try to create a personalized recommendation;) 
Check it out!
"""
st.markdown(description_movies)
st.markdown("Click below button to visit my app for recommending movies!!")
url_movies = "https://moviesrecommenderapp-by-yosuke.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_movies}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)


# AI agent to help planning travel
st.header("🌍 Travel plan AI agent")
st.subheader("Discription")
description_agent = """
#### Background
Since I love traveling and have been to already 33 counties, I've spent so much time on seaching where I could go next to explore with limited budget looking all over the youtube, flight tickets and hostels to find the best route.
So, I developed AI agent can suggest travel plan based on all of my conditions such as my interests, budget,  countries that I alredy visited, etc.
This Agent utilizes Gemini model so it requires Gemini API which is free of charge!!(I love Gemini API great appriciation for Google)
You can generate your Gemini API key [here](https://aistudio.google.com/app/apikey)

#### How to use it
1. Generate Gemini API key
2. Click 'Others' and input Gemini APi key on sidebar.
3. Chat with Agent!
"""
st.markdown(description_agent)
st.markdown("Click below button to visit my Travel plan AI agent!!")
url_agent = "https://i-will-assist-you-to-plan-traveling.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_agent}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)


# suggesting travel itinerary
st.header("🛫 Suggesting travel itinerary")
st.subheader("Discription")
description_itinerary = """
#### Background
Since I am a huge fun of traveling, I always spend a bunch of time of what to do during travel in my spare time.
Maybe you too??
Well, this app is a time saver to suggest travel itinerary for you!
This will give you a roughly idea of what you can do during travel.
This app utilizes Gemini model so it requires Gemini API which is free of charge!!
You can generate your Gemini API key [here](https://aistudio.google.com/app/apikey)

#### How to use it
1. Generate Gemini API key.
2. Click 'Others' and input Gemini APi key on sidebar.
3. Input your duration, destination, departure date. If you already decided next destination, input it too.
4. Click "Generate Itinerary" button.
"""
st.markdown(description_itinerary)
st.markdown("Click below button to visit my app for suggesting you an travel itinerary!!")
url_itinerary = "https://lets-make-travel-itinerary-together.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_itinerary}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)


# summarizing meeting minutes from audio file
st.header("📋 Summarizing meeting minutes from audio file")
st.subheader("Discription")
description_summary = """
#### Background
Have you ever thought that you wanted to automate creating meeting minutes especially when you attend international meetings where people speak different languages?
Well, this app is for you!!  
This app utilizes Gemini model so it requires Gemini API which is free of charge!!
You can generate your Gemini API key [here](https://aistudio.google.com/app/apikey)

#### How to use it
1. Record a meeting.
2. Generate Gemini API key
3. Input Gemini API key on sidebar.
4. Drop the audio file that records a meeting.
5. Select the original language that is spoken in the meeting and the target language that you want to summarize
6. Press the button

This way, you won't waste your precious time and it is completely free!!

"""
st.markdown(description_summary)
st.markdown("Click below button to visit my app for summarizing meeting meniuts from audio file!!")
url_summary = "https://summarizemeetingminutesapp-bzha9c2qlxsveh46xmeebm.streamlit.app/"
# Create a button with HTML
st.markdown(f"""
    <a href="{url_summary}" type="url_app" target="_blank" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #FFFF00; border-radius: 5px; text-decoration: none;">Try app</a>
""", unsafe_allow_html=True)

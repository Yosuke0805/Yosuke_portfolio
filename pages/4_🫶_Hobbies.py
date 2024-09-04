import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css("style/style.css")

# load profile image
img_profile = Image.open("images/profile_photo.jpg")
with st.sidebar:
    st.image(img_profile, width=200)
# TODO: Upload image on cloud to load by URL
# st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("🫶 Hobbies")

# config
travel_pic_path = "images/Cappadocia.jpeg"
snowboarding_path = "images/snowboading.jpg"
workout_path = "images/workout.JPG"

#################### using html ####################
# Sample data
data = [
    {"name": "Travel", "image": travel_pic_path},
    {"name": "Snowboaring", "image": snowboarding_path},
    {"name": "Workout", "image": workout_path}
]

# Creating a table with images

table = f"""
<table>
    <tr>
        <th>{data[0]["name"]}</th>
        <th>{data[1]["name"]}</th>
        <th>{data[2]["name"]}</th>
   </tr>
   <tr>
        <td>{data[0]["name"]}</td>
        <td>{data[1]["name"]}</td>
        <td>{data[2]["name"]}</td>   
    </tr>
"""

# for item in data:
#     table += f"""
# <table>
#     <tr>
#         <th>{item['name']}</th>
#         <td><img src="{item['image']}" width="100"></td>
#     </tr>
#     """

# table += "</table>"

# Display the table
st.markdown(table, unsafe_allow_html=True)

#################### using columns ####################
# load images
img_1 = Image.open(travel_pic_path)
img_2 = Image.open(snowboarding_path)
img_3 = Image.open(workout_path)

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Traveling")
   st.image(img_1)

with col2:
   st.subheader("Snowboarding")
   st.image(img_2)

with col3:
   st.subheader("Workout")
   st.image(img_3)


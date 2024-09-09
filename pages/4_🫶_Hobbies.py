import streamlit as st
from PIL import Image
from constant import *
import base64

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
travel_img_path = "images/lake_district.jpg"
snowboarding_img_path = "images/snowboarding.jpg"
workingout_img_path = "images/workout.JPG"

#################### using html ####################
# Sample data
data = [
    {"name": "Travel", "image": travel_img_path, "description": "I have been to 31 countries since I started traveling when I was 21."},
    {"name": "Snowboaring", "image": snowboarding_img_path, "description": "Currently mastering run trick with curving."},
    {"name": "Workout", "image": workingout_img_path, "description": "I love working out and doing lifting. I just love exercise which makes me release my stress and feel adrenaline."}
]

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

travel_img_base64 = get_base64_of_bin_file(data[0]["image"])
snowboarding_img_base64 = get_base64_of_bin_file(data[1]["image"])
workingout_img_base64 = get_base64_of_bin_file(data[2]["image"])

# Creating a table with images

table = f"""
<table>
    <tr>
        <th>{data[0]["name"]}</th>
        <th>{data[1]["name"]}</th>
        <th>{data[2]["name"]}</th>
   </tr>
   <tr>
        <td><img src="data:image/png;base64,{travel_img_base64}" style="height:300px;width:auto"></td>
        <td><img src="data:image/png;base64,{snowboarding_img_base64}" style="height:300px;width:auto"></td>
        <td><img src="data:image/png;base64,{workingout_img_base64}" style="height:300px;width:auto"></td>
    </tr>
    <tr>
        <th>{data[0]["description"]}</th>
        <th>{data[1]["description"]}</th>
        <th>{data[2]["description"]}</th>
   </tr>
"""

# Display the table
st.markdown(table, unsafe_allow_html=True)

#################### using columns ####################
# # load images
# img_1 = Image.open(travel_img_path)
# img_2 = Image.open(snowboarding_img_path)
# img_3 = Image.open(workingout_img_path)

# col1, col2, col3 = st.columns(3)

# with col1:
#    st.subheader("Traveling")
#    st.image(img_1)

# with col2:
#    st.subheader("Snowboarding")
#    st.image(img_2)

# with col3:
#    st.subheader("Workout")
#    st.image(img_3)


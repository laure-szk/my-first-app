
import streamlit as st
from streamlit_extras.three_viewer import *


from streamlit_extras.let_it_rain import *

st.header("Coin-Coin")

#la pluie d'étoiles
rain(
    emoji="🦆",
    font_size=54,
    falling_speed=5,
    animation_length="10s"
)

#le canard
st.write("##### Mon petit canard intéractif")
# Using a public GLB model from the Khronos glTF sample models
model_url = ("https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb")
three_viewer(model_url, height=400, key="basic_demo")
st.caption("Drag to rotate, scroll to zoom, right-click drag to pan.")
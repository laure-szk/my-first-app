# Photos slider
import streamlit as st
from streamlit_extras.keyboard_url import *
from streamlit_extras.image_compare_slider import *

st.header("❤️ I wish you a wonderfull day")

st.write("### Fait glisser pour regagner de la bonne humeur")
image_compare_slider(
    "https://images.unsplash.com/photo-1586336208625-cfa9d024c759?q=80&w=2052&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1661962858972-6f3303ebd748?q=80&w=1692&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    key="basic_compare",
    position=0
    )
  
# la touche de clavier
keyboard_to_url(key="L", url="https://www.laure-helene.fr")
load_key_css()
st.write(f"""🤫 If your are curious, hit {key("L", False)} on your keyboard...!""",
         unsafe_allow_html=True,)
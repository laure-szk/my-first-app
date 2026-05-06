import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.let_it_rain import *
from streamlit_extras.dataframe_explorer import *
from streamlit_extras.keyboard_url import *
from streamlit_extras.three_viewer import *
from streamlit_extras.image_compare_slider import *


st.title("Laure's Wonderfull app")


#la pluie d'étoiles
rain(
    emoji="✨",
    font_size=54,
    falling_speed=5,
    animation_length="10s"
)


####.  LES GRAPHIQUES

st.header("And now the serious things")
st.markdown("More information about France emission [here](https://www.iea.org/countries/france/emissions)")


selected_start_year, selected_end_year = st.slider('Select year range', min_value=1950, max_value=2011, value=(1950,2011))

df_co = pd.read_csv('data/CO2.csv', sep=";")
def top_n_emitters(start_year=2008, end_year=2011, nb_displayed=10):
    df_to_plot = df_co[(df_co['Year'] > start_year) & (df_co['Year'] < end_year)]\
        .groupby('Country Name', as_index=False)[['CO2 Per Capita (metric tons)']].mean()\
        .rename(columns={'CO2 Per Capita (metric tons)':'Mean CO2 per Country'})\
        .sort_values('Mean CO2 per Country',ascending=False)\
        .head(nb_displayed)
    return px.bar(df_to_plot, x='Country Name', y='Mean CO2 per Country', 
                  title=f"The 5 countries that generated the most CO2 between {selected_start_year} and {selected_end_year}")

fig_bar = top_n_emitters(start_year=selected_start_year, end_year=selected_end_year)
                         
st.plotly_chart(fig_bar)

fig_map = px.scatter_geo(df_co.dropna().sort_values('Year'),
    locations='Country Code',size='CO2 Per Capita (metric tons)',
    animation_frame='Year',
    hover_name='Country Name',
    title='Evolution of CO2 emission per capital over the years',
    projection='natural earth')

st.plotly_chart(fig_map)
st.write("Visu of the data")
st.dataframe(df_co.dropna(), width="stretch")



# Injection de CSS pour modifier la largeur de la sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 500px !important; /* Changez 400px par la largeur souhaitée */
    }
    </style>
    """,
    unsafe_allow_html=True
)
with st.sidebar:
  st.header("❤️ I wish you a wonderfull day")
  
  #le canard
  st.write("##### Mon petit canard intéractif")
  # Using a public GLB model from the Khronos glTF sample models
  model_url = ("https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb")
  three_viewer(model_url, height=400, key="basic_demo")
  st.caption("Drag to rotate, scroll to zoom, right-click drag to pan.")
  
  # la touche de clavier
  keyboard_to_url(key="L", url="https://www.laure-helene.fr")
  load_key_css()
  st.write(f"""🤫 If your are curious, hit {key("L", False)} on your keyboard...!""",
    unsafe_allow_html=True,)
  
  # Photos slider
  st.write("### Fait glisser pour regagner de la bonne humeur")
  #st.write("Drag the slider to compare the two images.")
  image_compare_slider(
      "https://images.unsplash.com/photo-1586336208625-cfa9d024c759?q=80&w=2052&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      "https://plus.unsplash.com/premium_photo-1661962858972-6f3303ebd748?q=80&w=1692&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      #label1="😔",
      #label2="🥰😄",
      key="basic_compare",
      position=0
      )


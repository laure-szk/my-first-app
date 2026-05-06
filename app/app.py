import streamlit as st

accueil = st.Page("pages/1_accueil.py", title="Accueil", icon="🏠")
dashboard = st.Page("pages/2_dashboard.py", title ="CO2 Dashboard", icon="🌏")
canard = st.Page("pages/3_Canard.py", title="Canard", icon="🦆")
humeur = st.Page("pages/4_Humeur.py", title="Humeur", icon="😊")

pg = st.navigation([accueil, dashboard, canard])
pg.run()
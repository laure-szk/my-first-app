
import streamlit as st
import pandas as pd
import plotly.express as px


####.  LES GRAPHIQUES

st.header("CO2 Dashboard")
st.markdown("More information about France emission [here](https://www.iea.org/countries/france/emissions)")

df_co = pd.read_csv('data/CO2.csv', sep=";")

fig_map = px.scatter_geo(df_co.dropna().sort_values('Year'),
    locations='Country Code',size='CO2 Per Capita (metric tons)',
    animation_frame='Year',
    hover_name='Country Name',
    title='Evolution of CO2 emission per capital over the years',
    projection='natural earth')

st.plotly_chart(fig_map)

selected_start_year, selected_end_year = st.slider('Select year range', min_value=1950, max_value=2011, value=(1950,2011))

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


st.write("Visu of the data")
st.dataframe(df_co.dropna(), width="stretch")


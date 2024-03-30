import streamlit as st
import pandas as pd
from Helper import helper
import folium
import geopandas as gpd
from streamlit_folium import folium_static



world = gpd.read_file('../Data/Map Files/ne_10m_admin_0_countries.shp')
df = pd.read_csv('../Data/Excel/medal_count.csv')

def map():
    st.sidebar.title('Olympic Analysis')
    st.sidebar.header('Medal Tally')
    year = helper.year_list(df)
    selected_year = st.sidebar.selectbox('Select a Year',year)
    medal_tally = helper.fetch_medal(df,selected_year)


    st.title('Olympic Data Visualization on map')

    merged_data = world.merge(medal_tally, left_on='SOVEREIGNT', right_on='Country')

    # Get the centroid of a specific country (e.g., 'United States of America')
    center_country = 'Spain'
    center_row = merged_data[merged_data['Country'] == center_country].iloc[0]
    center_location = [center_row['geometry'].centroid.y - 0.1, center_row['geometry'].centroid.x]  # Slight downward adjustment


    map_olympics = folium.Map(center_location, zoom_start=2)


    # Add GeoJSON layers for countries with hover tooltips
    for idx, row in merged_data.iterrows():
        country_name = row['Country']
        total_win = row['Total']
        tooltip_text = f"<div style='font-size: 16px;'>Country: {country_name}<br>Total Medal Wins: {total_win}</div>"


        # Create a GeoJSON layer for the country with the tooltip
        country_layer = folium.GeoJson(row['geometry'],
                                       style_function=lambda x: {
                                           'fillColor': 'cyan',
                                           'color': 'black',
                                           'weight': 1,
                                           'fillOpacity': 0.6
                                       },
                                       highlight_function=lambda x: {
                                           'weight': 3,
                                           'color': 'blue'
                                       },
                                       tooltip=tooltip_text
                                       )

        # Add the country layer to the map
        country_layer.add_to(map_olympics)

    # Display the map
    st.markdown('### Olympic Events Map for ' + str(selected_year))
    folium_static(map_olympics , width=1100, height=700)


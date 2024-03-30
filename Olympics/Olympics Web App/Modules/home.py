import streamlit as st
from Helper import countdown



def homepage():

    col1,col2,col3 = st.columns(3)
    with col2:
        st.title("Olympic Data Analysis")
    st.markdown("***")
    st.text(" ")


    col1,col2,col3 = st.columns([7,1,7])
    with col1:
        st.markdown("## Introduction")
        st.markdown("##### The Olympic Games are the world's only truly global, multi-sport, celebratory athletics competition. With more than 200 countries participating in over 400 events across the Summer and Winter Games, the Olympics are where the world comes to compete, feel inspired, and be together. Olympic games are considered as one of the most prime events which provides a valid and common platform for players across different countries to show their talent and skills. This Event is held every 4 years, Analyzing its data can provide valuable insights into athlete performance, medal counts, historical trends, and other factors that influence the outcome of the games.")
    with col3:
        col1,col2,col3 = st.columns(3)
        with col1:
            st.image("https://images.pexels.com/photos/7866131/pexels-photo-7866131.jpeg?auto=compress&cs=tinysrgb&w=600", use_column_width=True)
        with col2:
            st.image("https://media.istockphoto.com/id/1320348199/photo/sign-of-olympic-rings-symbol-of-olympics-in-urban-environment.jpg?s=612x612&w=0&k=20&c=DyC1E3gNVvZtW7zjJjFqG3g8O-M-dTYzjhGxaHnGKpQ=", use_column_width=True)
        with col3:
            st.image("https://images.pexels.com/photos/8820625/pexels-photo-8820625.jpeg?auto=compress&cs=tinysrgb&w=600", use_column_width=True)


    st.markdown(" ")
    st.markdown("***")
    st.markdown(" ")


    col1,col2,col3 = st.columns([7,1,7])
    with col1:
        col4,col5 = st.columns(2)
        with col4:
            st.image("https://media.istockphoto.com/id/1156240802/photo/three-businessman-working-and-discussing-business-together-in-a-meeting.jpg?b=1&s=612x612&w=0&k=20&c=80PUG7eic6qNPnpIVyZpOeuksphP5K9c1pd-HRmmZjo=", use_column_width=True)
        with col5:
            st.image("https://media.istockphoto.com/id/1418476287/photo/businessman-analyzing-companys-financial-balance-sheet-working-with-digital-augmented-reality.jpg?b=1&s=612x612&w=0&k=20&c=DfSCIoYtn5f7WcEwsZR-CtA9tY5dEA45rKs60yIKjJU=", use_column_width=True)
    with col3:
        st.markdown("## Overview")
        st.markdown("##### Welcome to the Olympic Data Analysis project! This application provides an overview of Olympic data, including historical data, statistics, and visualizations. This Event is held every 4 years, Analyzing its data can provide valuable insights into athlete performance, medal counts, historical trends, and other factors that influence the outcome of the games.")


    st.markdown("***")
    st.markdown(" ")
    st.markdown(" ")


    col1,col2,col3 = st.columns([7,1,7])
    with col1:
        st.markdown("## Valuable insights")
        st.markdown("##### Here, you'll find various data analysis and visualizations related to the Olympics. We extract valuable insights, uncover hidden patterns, and present the information in a way that is understandable and accessible to a wide audience. It has a prediction model that is accurate which can effectively forecast future Olympic games medalists. We are also interested in developing a geospatial data visualization platform, where data is represented on a map.")
    with col3:
        col1,col2 = st.columns(2)
        with col1:
            st.image("https://media.istockphoto.com/id/1186972049/photo/new-idea-on-the-puzzle-piece.jpg?b=1&s=612x612&w=0&k=20&c=dkfjeI55akjVkKRd6mj2k_hIWg3Xp7Z759HyVGqG2xw=",use_column_width=True)
        with col2:
            st.image("https://media.istockphoto.com/id/1304835378/photo/innovative-idea.jpg?b=1&s=612x612&w=0&k=20&c=wyU6JDp3Q9KZ3w_D-549kqibDtdukdgj81QJg3jgB7k=",use_column_width=True)


    st.markdown(" ")
    st.markdown("***")
    st.markdown(" ")


    col1, col2, col3 = st.columns([7, 1, 7])
    with col1:
        col4, col5 = st.columns(2)
        with col4:
            st.image(
                "https://medias.paris2024.org/uploads/2023/08/OLY-GRAND-PALAIS-16_9-3.png?x-oss-process=image/resize,w_2000,h_1125,m_lfit/format,png",
                use_column_width=True)
        with col5:
            st.image(
                "https://fattirebiketours.com/app/uploads/2021/11/paris-olympics-eiffel-tower-2024.jpg",
                use_column_width=True)
    with col3:
        st.markdown("## Paris Olympics")
        st.markdown("##### Welcome to the Olympic Data Analysis project! This application provides an overview of Olympic data, including historical data, statistics, and visualizations. This Event is held every 4 years, Analyzing its data can provide valuable insights into athlete performance, medal counts, historical trends, and other factors that influence the outcome of the games.")

    st.text('')
    st.text('')
    countdown.countdown()

    st.markdown("***")

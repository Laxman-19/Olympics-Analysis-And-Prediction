import streamlit as st
from streamlit_option_menu import option_menu
import home, analyze, map, prediction, about
import base64

st.set_page_config(layout="wide", page_title='Olympics', page_icon='🏅',)

selected = option_menu(
    menu_title = None,
    options = ['Home','Analysis','Map','Prediction','About Us'],
    icons = ['house-door-fill','bar-chart-fill','globe-central-south-asia','easel2-fill','file-person-fill'],
    default_index = 0,
    orientation = 'horizontal',
    styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#1d9bf0"},
    }
)


if selected == 'Home':
    home.homepage()


if selected == 'Analysis':
    analyze.analysisPage()


if selected == 'Map':
    map.map()


if selected == 'Prediction':
    prediction.predict()


if selected == 'About Us':
    about.about_us()

















# hide_st_style = """
# <style>
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('../Data/Image/z_bg_img.avif')


footer = """
<style>
a:link, a:visited {
    color: blue;
    background-color: transparent;
    text-decoration: none;
}
a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: none;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.9);
    text-align: center;
}
.footer-content a {
    display: inline-block;
    margin: 0 10px; 
}
</style>

<div class="footer">
    <div class="footer-content">
        <h6 style="display: inline;">Developed by </h6>
        <a href="https://www.linkedin.com/in/niharika-sahu-677511261/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"><i>📷 Niharika Sahu</i></a>
        <a href="https://www.linkedin.com/in/harish-sargar-09500124b/"><i>📷 Harish Sargar</i></a>
        <a href="https://www.linkedin.com/in/laxman-sawant-010356245/"><i>📷 Laxman Sawant</i></a>
    </div>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)






header = """
<style>
a:link, a:visited {
    color: black;
    background-color: transparent;
    text-decoration: none;
}
a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: none;
}
.header {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 50px;
    background-color: rgba(255, 255, 255, 0.9);
    text-align: left;
}
.header a {
    display: inline-block;
    margin: 0 10px; 
}
</style>

<div class="header">
    <h3><a href="https://olympics.com/en/">⚽ Olympics</a></h3>
</div>
"""
st.markdown(header, unsafe_allow_html=True)



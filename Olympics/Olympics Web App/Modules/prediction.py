import streamlit as st
import pandas as pd
import joblib
from Helper import helper

df = pd.read_csv('../Data/Excel/processed_data.csv')

country_list = helper.country_list(df)
sports_list = helper.sports_list(df)

def predict():
	st.markdown("<h1 style='text-align: center;'>Olympic Prediction</h1>", unsafe_allow_html=True)
	st.markdown("***")

	col1, col2, col3, col4, col5 = st.columns([3,1,3,1,3])
	with col1:
		st.markdown("### Enter the age")
		age = st.number_input('Enter your current Age')
	with col3:
		st.markdown("### Enter the Weight")
		weight = st.number_input('Enter your most recent Weight (in lbs)')
	with col5:
		st.markdown("### Enter the Height")
		height = st.number_input('Enter your most recent Height (in cms)')

	st.text('')
	st.text('')

	col1, col2, col3, col4, col5 = st.columns([3,1,3,1,3])
	with col1:
		st.markdown("### Select your Gender")
		gender = st.selectbox('Make sure to select only between these two', ('Male', 'Female'))
	with col3:
		st.markdown("### Select your Country")
		country = st.selectbox('Select the Country which you will be representing', country_list)
	with col5:
		st.markdown("### Select your Sport")
		sport = st.selectbox('Select the Sport which you will be playing', sports_list)

	st.text('')
	st.markdown("***")
	st.text('')

	if st.button('Predict'):

		model = joblib.load('../Data/Pickle Data/model.pkl')
		gender_loaded = joblib.load('../Data/Pickle Data/gender.pkl')
		country_loaded = joblib.load('../Data/Pickle Data/country.pkl')
		sport_loaded = joblib.load('../Data/Pickle Data/sport.pkl')

		gender_encoded = gender_loaded.transform([gender])[0]
		country_encoded = country_loaded.transform([country])[0]
		sport_encoded = sport_loaded.transform([sport])[0]

		data = pd.DataFrame([int(gender_encoded), int(age), int(height), int(weight), int(country_encoded), int(sport_encoded)], index=['Gender', 'Age', 'Height', 'Weight', 'Country', 'Sport'])
		data = data.T

		predicted_medal = model.predict(data)[0]

		if predicted_medal == 'Gold':
			st.markdown("<h2 style='text-align: center;'>Congratulations! You are 84% likely to win a Gold Medal!</h2>", unsafe_allow_html=True)
		elif predicted_medal == 'Silver':
			st.markdown("<h2 style='text-align: center;'>You are 84% likely to a Silver Medal!</h2>", unsafe_allow_html=True)
			st.markdown("<h3 style='text-align: center;'>Keep working hard.</h3>", unsafe_allow_html=True)
		elif predicted_medal == 'Bronze':
			st.markdown("<h2 style='text-align: center;'>You are 84% likely to a Bronze Medal!</h2>", unsafe_allow_html=True)
		else:
			st.markdown("<h2 style='text-align: center;'>Unfortunately, You are 84% likely not to win any medal.</h2>", unsafe_allow_html=True)
			st.markdown("<h3 style='text-align: center;'>Dont worry its just a model. There are still 16% chances.</h3>", unsafe_allow_html=True)


import pandas as pd
import joblib


def AthletePred():

    model = joblib.load('../Data/Pickle Data/model.pkl')
    gender_loaded = joblib.load('../Data/Pickle Data/gender.pkl')
    country_loaded = joblib.load('../Data/Pickle Data/country.pkl')
    sport_loaded = joblib.load('../Data/Pickle Data/sport.pkl')


    age = input("Enter the Athlete's Age: ")
    gender = input("Enter the Athlete's Gender: ")
    height = input("Enter the Athlete's Height cm: ")
    weight = input("Enter the Athlete's Weight lbs: ")
    country = input("Enter the Athlete's Country: ")
    sport  = input("Enter the Athlete's Sport: ")


    gender_encoded = gender_loaded.transform([gender])[0]
    country_encoded = country_loaded.transform([country])[0]
    sport_encoded = sport_loaded.transform([sport])[0]

    data = pd.DataFrame([int(gender_encoded), int(age), int(height), int(weight), int(country_encoded), int(sport_encoded)], index =['Gender', 'Age', 'Height', 'Weight', 'Country', 'Sport'])
    data = data.T
    

    predicted_medal = model.predict(data)[0]
    
    if predicted_medal == 'Gold':
        return 'Congratulations! You are 84% likely to win a Gold Medal!'
    elif predicted_medal == 'Silver':
        return 'You are 84% likely to a Silver Medal!'
    elif predicted_medal == 'Bronze':
        return 'You are 84% likely to a Bronze Medal!'
    else:
        return 'Unfortunately, You are 84% likely not to win a medal.'


import pandas as pd

def preprocess(df,region_df,tokyo_df):
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)

    df = df.drop(['ID', 'Team', 'Games', 'Season', 'City', 'Event', 'notes'], axis=1)
    df = df.rename(columns={'Sex': 'Gender', 'region': 'Country'})
    df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female', })
    df = df[['Name', 'Gender', 'Age', 'Height', 'Weight', 'Year', 'Country', 'NOC', 'Sport', 'Medal']]

    tokyo_df = tokyo_df.drop(['Unnamed: 0', 'Code', 'Discipline', 'Event', 'Rank'], axis=1)
    tokyo_df['Year'] = 2020
    tokyo_df = tokyo_df[['Name', 'Gender', 'Age', 'Year', 'Country', 'NOC', 'Sport', 'Medal']]

    result_df = pd.concat([df, tokyo_df], axis=0)
    result_df.reset_index(drop=True, inplace=True)

    x = pd.get_dummies(result_df['Medal']).astype(int)
    result_df = pd.concat([result_df, x], axis=1)
    result_df.drop_duplicates(inplace=True)

    result_df['Total'] = result_df['Gold'] + result_df['Silver'] + result_df['Bronze']
    result_df = result_df[['Name', 'Gender', 'Age', 'Height', 'Weight', 'Year', 'Country', 'NOC', 'Sport', 'Medal', 'Gold', 'Silver','Bronze', 'Total']]

    return result_df


# The above preprosses code provide you a dataframe(same dataframe is stored in "processed_data.csv").
# But the code is mentioned above (as in how the "processed_data.csv" is formed).
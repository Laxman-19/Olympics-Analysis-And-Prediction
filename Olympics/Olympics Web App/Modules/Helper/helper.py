import pandas as pd

def year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    return years

def country_list(df):
    country = df['Country'].dropna().unique().tolist()
    country.sort()
    country.insert(0, 'Overall')
    return country

def sports_list(df):
    sports = df['Sport'].unique().tolist()
    sports.sort()
    sports.insert(0, 'Overall')
    return sports









# Medal Tally start.

def fetch_medal_history(df,year,country):

    flag = 0
    medal_df = df.drop_duplicates(subset=['Year','Country','Team','Games','Sport','Event','Medal'])

    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['Country'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == year]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Country'] == country) & (medal_df['Year'] == year)]

    if flag == 1:
        medal_tally = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze','Total']].sort_values('Year').reset_index()
    else:
        medal_tally = temp_df.groupby('Country').sum()[['Gold','Silver','Bronze','Total']].sort_values('Gold',ascending=False).reset_index()

    return medal_tally

# Medal Tally end.









# Overall Analysis start.

def countries_over_years(df):
    countries = df.drop_duplicates(['Year','Country'])['Year'].value_counts().reset_index().sort_values('Year')
    countries.rename(columns={'Year':'Edition','count':'No. of Countries'},inplace=True)
    return countries

def athletes_over_years(df):
    athletes = df.drop_duplicates(['Year','Name'])['Year'].value_counts().reset_index().sort_values('Year')
    athletes.rename(columns={'Year':'Edition','count':'No. of Athletes'},inplace=True)
    return athletes

def sports_over_years(df):
    sports = df.drop_duplicates(['Year', 'Sport'])['Year'].value_counts().reset_index().sort_values('Year')
    sports.rename(columns={'Year':'Edition','count':'No. of Sports'},inplace=True)
    return sports

def events_over_years(df):
    events = df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values('Year')
    events.rename(columns={'Year':'Edition','count':'No. of Events'},inplace=True)
    return events

def most_successful_athlete(df, sport):
    aa = df.dropna(subset=['Medal'])
    bb = aa.groupby('Name')['Total'].sum().reset_index().sort_values('Total', ascending=False)

    cc = df.drop_duplicates(subset=['Name', 'Sport'])
    cc = cc.drop(['Total'],axis=1)
    dd = pd.merge(bb, cc, left_on='Name', right_on='Name', how='left')

    temp_df = dd[['Name', 'Total', 'Sport', 'Country']]
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    temp_df = temp_df.rename(columns={'Total':'Medals','Country':'Country'})
    temp_df = temp_df.reset_index()
    temp_df = temp_df.rename(columns={'index':'Rank'})

    # return temp_df[['Name','Medals','Sport','Country']].head(15)
    return temp_df.head(15)

# Overall Analysis end.









# Country Wise start.

def country_wise_medal_display(df,country):
    medal_list = df[df['Country'] == country]
    medal_list = medal_list.groupby('Year').sum()[['Total']].sort_values('Year').reset_index()
    # Another way you can do this is (It is for country != Overall) :
    # a = df.dropna(subset=['Medal'])
    # b = a.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    # c = b[b['Country'] == country]
    # d = c.groupby('Year').count()['Medal'].reset_index()
    medal_list.rename(columns={'Total':'No. of Medals'},inplace=True)
    return medal_list

def top10_athletes_countrywise(df, country):
    aa = df.dropna(subset=['Medal'])
    bb = aa.groupby('Name')['Total'].sum().reset_index().sort_values('Total', ascending=False)
    cc = df.drop_duplicates(subset=['Name', 'Sport'])
    cc = cc.drop(['Total'], axis=1)
    dd = pd.merge(bb, cc, left_on='Name', right_on='Name', how='left')

    temp_df = dd[['Name', 'Total', 'Country', 'Sport']]
    if country != 'Overall':
        temp_df = temp_df[temp_df['Country'] == country]
    temp_df = temp_df.rename(columns={'Total':'Medals','Country':'Country'})

    temp_df = temp_df.reset_index()

    return temp_df[['Name','Medals','Country','Sport']].head(10)

# Country Wise end.









# Athlete Wise start.

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'Country'])

    men = athlete_df[athlete_df['Gender'] == 'Male'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Gender'] == 'Female'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final

# Athlete Wise end.









# Year Wise start.

def year_wise_medal_display(df,year):
    if year == 'Overall':
        medal_list = df
        # medal_list = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
        medal_list = medal_list.groupby('Country').sum()[['Total']].sort_values('Country').reset_index()
    if year != 'Overall':
        medal_list = df
        medal_list = df[df['Year'] == year]
        # medal_list = medal_list.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
        medal_list = medal_list.groupby('Country').sum()[['Total']].sort_values('Country').reset_index()
    medal_list.rename(columns={'Country':'Country','Total':'No. of Medals'},inplace=True)
    return medal_list

# Year Wise end.









# Map start.

def fetch_medal(df,year):

    df = df.drop(['Name'], axis=1)

    medal_df = df.drop_duplicates(subset=['Team','Games','Year','City','Sport','Event','Medal'])
    medal_df['Country'] = medal_df['Country'].replace('USA', 'United States of America')

    if (year == 'Overall'):
        temp_df = medal_df
    elif (year != 'Overall'):
        temp_df = medal_df[medal_df['Year'] == year ]
                         
    x = temp_df.groupby('Country').sum()[['Gold','Silver','Bronze','Total']].sort_values('Gold',ascending=False).reset_index()

    return x
 
# Map end.




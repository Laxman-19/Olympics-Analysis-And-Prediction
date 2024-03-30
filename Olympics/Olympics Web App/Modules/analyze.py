import streamlit as st
import pandas as pd
from Helper import helper, preprocessor
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.figure_factory import create_distplot

# raw_df = pd.read_csv('Data/Excel/athlete_events.csv')
# country_df = pd.read_csv('Data/Excel/noc_regions.csv')
# tokyo_df = pd.read_csv('Data/Excel/tokyo_dataset.csv', encoding='latin1')
# df1 = preprocessor.preprocess(raw_df,country_df,tokyo_df)

medal_df = pd.read_csv('../Data/Excel/medal_count.csv')
df = pd.read_csv('../Data/Excel/processed_data.csv')

def analysisPage():

    st.sidebar.title('Olympics Analysis')
    st.sidebar.image('https://blog.ipleaders.in/wp-content/uploads/2017/07/BV-Acharya-90.jpg')
    options = ['Medal Tally','Overall Analysis','Country Wise Analysis','Athlete Wise Analysis','Year Wise Analysis']
    user_menu = st.sidebar.radio('Select an Option', options)





    if user_menu == 'Medal Tally':
        st.sidebar.header('Medal Tally')
        years_list = helper.year_list(df)
        country_list = helper.country_list(df)

        selected_year = st.sidebar.selectbox('Select the Year', years_list)
        selected_country = st.sidebar.selectbox('Select the Country', country_list)

        if selected_year == 'Overall' and selected_country == 'Overall':
            st.title("Overall Tally")
        if selected_year != 'Overall' and selected_country == 'Overall':
            st.title("Medal Tally in " + str(selected_year) + " Olympics")
        if selected_year == 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " overall performance")
        if selected_year != 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        medal_tally = helper.fetch_medal_history(medal_df, selected_year, selected_country)
        st.table(medal_tally)





    if user_menu == 'Overall Analysis':
        st.sidebar.header('Overall Tally')
        editions = len(df['Year'].unique())
        cities = len(medal_df['City'].unique())
        sports = len(df['Sport'].unique())
        events = len(medal_df['Event'].unique())
        athletes = len(df['Name'].unique())
        nations = len(df['Country'].unique())

        col1, col2, col3 = st.columns([3, 4, 1])
        with col2:
            st.title("Top Statistics")
        st.markdown('***')

        col1, col2, col3, col4 = st.columns([1,2,2,2])
        with col2:
            st.subheader("Editions")
            st.header(editions)
            st.text('')
            st.text('')
        with col3:
            st.subheader("Hosts")
            st.header(cities)
        with col4:
            st.subheader("Sports")
            st.header(sports)

        col1, col2, col3, col4 = st.columns([1,2,2,2])
        with col2:
            st.subheader("Events")
            st.header(events)
        with col3:
            st.subheader("Nations")
            st.header(nations)
        with col4:
            st.subheader("Athletes")
            st.header(athletes)

        st.markdown('<hr style="height:1px; background-color:#000000;">', unsafe_allow_html=True)
        st.text('')


        col1, col2, col3, col4 = st.columns([1,6,1,6])
        with col2:
            st.subheader('Participating Countries over the Years')
            countries = helper.countries_over_years(df)
            fig1 = px.line(countries, x="Edition", y="No. of Countries")
            fig1.update_layout(width=500,height=400,)
            st.plotly_chart(fig1)
            st.markdown('This line chart depicts the evolution of Countries participation across Olympic editions, showcasing the Games growth and scale over time.')
            st.markdown('***')
        with col4:
            st.subheader('No. of Athletes over Years')
            athletes = helper.athletes_over_years(df)
            fig2 = px.bar(athletes, x='Edition', y='No. of Athletes')
            fig2.update_layout(width=500,height=400,)
            st.plotly_chart(fig2)
            st.markdown('This bar chart tracks the changing number of athletes across different Olympic editions, revealing the Olympics evolving scale over time.')
            st.markdown('***')


        col1, col2, col3, col4 = st.columns([1,6,1,6])
        with col2:
            st.subheader('No. of Sports over Years')
            sports = helper.sports_over_years(df)
            fig1 = px.histogram(sports, x="Edition", y="No. of Sports")
            fig1.update_layout(width=500, height=400,)
            st.plotly_chart(fig1)
            st.markdown('This histogram chart portrays the growth of sports diversity in the Olympics over different editions by associating the number of Olympic events with the range of sports they encompass, offering insights into the Games evolution and expansion.')
        with col4:
            st.subheader('No. of Events over Years')
            events = helper.events_over_years(medal_df)
            fig2 = px.area(events, x="Edition", y="No. of Events")
            fig2.update_layout(width=500, height=400,)
            st.plotly_chart(fig2)
            st.markdown('This area chart visually represents the number of Olympic editions on the horizontal x-axis and the count of sporting events on the vertical y-axis, providing an overview of how the diversity of Olympic events has evolved over time.')

        st.markdown('<hr style="height:1px; background-color:#000000;">', unsafe_allow_html=True)
        st.text('')

        st.subheader('Most Successfull Athletes (Sport Wise)')
        sports_list = helper.sports_list(df)
        selected_sport = st.selectbox('Select the Sport', sports_list)
        successful_athlete = helper.most_successful_athlete(df, selected_sport)
        st.table(successful_athlete)





    if user_menu == 'Country Wise Analysis':
        st.sidebar.header('Country Wise Tally')

        country_list = df['Country'].dropna().unique().tolist()
        country_list.sort()
        selected_country = st.sidebar.selectbox('Select the Country', country_list)

        col1, col2, col3 = st.columns([2, 5, 1])
        with col2:
            st.subheader('Total medals won by ' + str(selected_country) + ' throughout Olympics')

        st.markdown('<hr style="height:1px; background-color:#000000;">', unsafe_allow_html=True)


        col1, col2, col3, col4 = st.columns([1, 6, 1, 6])
        with col2:
            st.subheader('Bar Graph')
            x = helper.country_wise_medal_display(df, selected_country)
            fig1 = px.bar(x, x="Year", y="No. of Medals")
            fig1.update_layout(width=500, height=400, )
            st.plotly_chart(fig1)
            st.markdown(f'##### It is a Bar graph representing Medal won by {selected_country} throughout.')
            st.divider()
        with col4:
            st.subheader('Line Graph')
            x = helper.country_wise_medal_display(df, selected_country)
            fig2 = px.line(x, x="Year", y="No. of Medals")
            fig2.update_layout(width=500, height=400, )
            st.plotly_chart(fig2)
            st.markdown(f'##### It is a Line graph representing Medal won by {selected_country} throughout.')
            st.divider()
        st.markdown('#### Both of the above graphs provide a visual representation of the medals won by individual countries over the course of multiple Olympic Games. These graphs offer valuable insights into the trends and patterns of medal achievements by different nations.')

        st.markdown('<hr style="height:1px; background-color:#000000;">', unsafe_allow_html=True)
        st.subheader('Top 10 Athletes of ' + selected_country)
        top_athletes = helper.top10_athletes_countrywise(df, selected_country)
        st.table(top_athletes)
        st.markdown('<hr style="height:1px; background-color:#000000;">', unsafe_allow_html=True)





    if user_menu == 'Athlete Wise Analysis':
        st.sidebar.header('Athlete Wise Tally')
        athlete_df = df.drop_duplicates(subset=['Name', 'Country'])

        x1 = athlete_df['Age'].dropna()
        x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
        x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
        x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

        fig = create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=800, height=400)
        st.header("Distribution of Age")
        st.plotly_chart(fig)

        x = []
        name = []
        famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                         'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                         'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                         'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                         'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                         'Tennis', 'Golf', 'Softball', 'Archery',
                         'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                         'Rhythmic Gymnastics', 'Rugby Sevens',
                         'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
        for sport in famous_sports:
            temp_df = athlete_df[athlete_df['Sport'] == sport]
            x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
            name.append(sport)

        fig1 = create_distplot(x, name, show_hist=False, show_rug=False)
        fig1.update_layout(autosize=False, width=800, height=400)
        st.header("Distribution of Age wrt Sports(Gold Medalist)")
        st.plotly_chart(fig1)

        sports_list = helper.sports_list(df)

        st.title('Height Vs Weight')


        st.header("Men Vs Women Participation Over the Years")
        final = helper.men_vs_women(df)
        fig3 = px.line(final, x="Year", y=["Male", "Female"])
        fig3.update_layout(autosize=False, width=800, height=400)
        st.plotly_chart(fig3)






    if user_menu == 'Year Wise Analysis':
        year_list = helper.year_list(df)
        selected_year = st.selectbox('Select the Year', year_list)
        if selected_year == 'Overall':
            st.subheader('Total medals won by countries in 120 Years')
        if selected_year != 'Overall':
            st.subheader('Total medals won by countries in ' + str(selected_year))
        x = helper.year_wise_medal_display(df, selected_year)
        fig = px.bar(x, x="Country", y="No. of Medals")
        st.plotly_chart(fig)



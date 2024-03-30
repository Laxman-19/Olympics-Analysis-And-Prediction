import streamlit as st

def about_us():

    st.text('')
    st.markdown('### About US')
    with open('../Data/team-description.txt', 'r') as file:
        file_contents = file.read()
    st.markdown(file_contents)
    st.divider()


    st.markdown("### About This Project")
    with open('../Data/project-description.txt', 'r') as file:
        file_contents = file.read()
    st.markdown(file_contents)
    st.divider()


    st.subheader("Meet the Team")
    st.text('')
    st.text('')

    col1, col2, col3, col4 = st.columns([1,5,5,5])
    with col2:
        st.image("../Data/Image/prof-img-laxman.jpg", width=300)
        st.markdown('#### Laxman Sawant')
        st.markdown('Team Member')
        st.markdown('9757119477')
        st.markdown('laxman19.sawant@gmail.com')
        st.markdown('Computer Science Engineer')
    with col3:
        st.image("../Data/Image/prof-img-niharika.jpeg", width=300)
        st.markdown('#### Niharika Sahu')
        st.markdown('Team Member')
        st.markdown('9022220385')
        st.markdown('sahuniharika1111@gmail.com')
        st.markdown('Computer Science Engineer')
    with col4:
        st.image("../Data/Image/prof-img-harish.jpeg", width=300)
        st.markdown('#### Harish Sargar')
        st.markdown('Team Member')
        st.markdown('8237169865')
        st.markdown('harishsargar19@gmail.com')
        st.markdown('Computer Science Engineer')

    st.divider()
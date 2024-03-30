import streamlit as st
from streamlit.components.v1 import html


my_html = """
<script>
function startTimer(endDate, display) {
    setInterval(function () {
        var currentDate = new Date();
        var timeDifference = endDate - currentDate;

        if (timeDifference <= 0) {
            display.textContent = "Countdown expired!";
            return;
        }

        var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        var hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

        days = days < 10 ? "0" + days : days;
        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = "Countdown : "  +days + "Day " + hours + "Hr " + minutes + "Min " + seconds + "Sec";
    }, 1000);
}

window.onload = function () {
    var endDate = new Date("July 26, 2024 00:00:00").getTime();
    var display = document.querySelector('#time');
    startTimer(endDate, display);
};
</script>

<style>
    #time {
        font-size: 35px; /* Adjust the font size here */
        font-family: "Courier New", Courier, monospace;
    }
</style>

<body>
  <div> <span id="time">00d 00h 00m 00s</span></div>
</body>


"""

def countdown():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown(" ")
        original_title = '<p style="font-family:Barlow Condensed; color:black; font-size: 45px; ">#ROADTOPARIS2024</p>'
        st.markdown(original_title, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 6])
    st.markdown(" ")
    st.markdown(" ")
    with col1:
        st.image("https://img.olympics.com/images/image/private/t_s_w440/f_auto/primary/gpo3co3bpkqsikyznrns",use_column_width=True)
    with col2:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")

        col3, col4 = st.columns([1, 1])
        with col3:
            original_title = '<p style="font-family:Barlow Condensed; color:black; font-size: 45px; ">Olympic Games Paris 2024 : </p>'
            st.markdown(original_title, unsafe_allow_html=True)
        with col4:
            original_title = '<p style="font-family:Barlow Condensed; color:black; font-size: 45px; ">26 July - 11 August, 2024 </p>'
            st.markdown(original_title, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 9, 1])
        with col2:
            html(my_html)
        st.markdown('### The most eagerly anticipated Olympic event is just around the corner, and the excitement is building. Get ready to witness extraordinary athletic performances and unforgettable moments')


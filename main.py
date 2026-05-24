import streamlit as st
st.set_page_config(
    page_title="Hassan's AI Dashboard",
    page_icon="📻",
    layout="wide"
)
st.title("📻 Hassan's AI Automation Dashboard")
st.subheader("My 3 AI Automation Real World Projects - All in One!")

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### 🕵️ GitHub Analyzer\nAnalyze any GitHub profile")
    if st.button("Open GitHub Tool", key="gh"):
        st.switch_page("pages/1_GitHub.py")

with col2:
    st.success("### 🌤️ Weather App\nReal-time weather data")
    if st.button("Open Weather Tool", key="weather"):
        st.switch_page("pages/2_Weather.py")

with col3:
    st.warning("### 📚 Book Scrapper\nBooks data visualization")
    if st.button("Open Scraper Tool", key="books"):
        st.switch_page("pages/3_Books.py")

st.markdown("---")
st.caption("Built with Python + Streamlit | AI Automation Engineer in Progress")
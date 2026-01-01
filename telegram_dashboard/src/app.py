import streamlit as st

st.title(":computer: Dashboard Project")
with st.expander("Upload File"):
    raw_data = st.file_uploader("Data")

import streamlit as st

st.title(":computer: Statistics Project")
with st.expander("Upload Your File Here"):
    st.file_uploader("Data")

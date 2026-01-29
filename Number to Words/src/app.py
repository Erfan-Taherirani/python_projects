import streamlit as st


from main import num_2_words


st.title("Number to Words Convertor")

st.markdown(">This dashboard is for the conversion of numbers to the words.")

number = st.text_input("Please Enter a Number:", 100)
if number:
    words = num_2_words(int(number))
    st.metric("In Words:", words)
else:
    st.write("No Number Entered")

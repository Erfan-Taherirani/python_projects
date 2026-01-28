import streamlit as st


from datetime import datetime


from constants import CURRENCIES
from currency_convertor import get_currencies_info, convert_currency


st.title(":dollar: Currency Convertor")

st.markdown("A real-time currency converter built with Python that delivers\
            accurate exchange rates through a simple and intuitive dashboard.")

base_currency = st.selectbox("From Currency (Base)", CURRENCIES)
target_currency = st.selectbox("To Currency (Target)", CURRENCIES)
amount = st.number_input("Amount", min_value=0.0, value=1.0)

exchange_rate, time_last_updated = get_currencies_info(base_currency, target_currency)

if exchange_rate:
    converted_amount = amount * exchange_rate
    st.success(f":white_check_mark: Exchange Rate: {exchange_rate: .4f}")
    st.success(f"Last Update: {datetime.fromtimestamp(time_last_updated)}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Base Currency", value=f"{amount: .3f} {base_currency}")
    col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
    col3.metric("Target Currency", value=f"{converted_amount: .3f} {target_currency}")
else:
    print("Error fetching exchange rate.")

import streamlit as st

st.write("Retail business dashboard")

st.header("Header")
st.write("MESSAGE")

age = st.number_input("Enter Monyhly sales target (in usd):",
                      min_value=0,
                      max_value=100000,
                      value=50000)


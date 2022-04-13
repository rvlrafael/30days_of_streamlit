import streamlit as st

# Create a header text
st.header('st-button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

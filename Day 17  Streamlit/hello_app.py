import streamlit as st
st.title("Hello, Streamlit!")
st.header("I am a webpage written in python")
st.write("The whole page is just a python")
st.write("Two plus two is:",2+2)
st.markdown("Streamlit understands **markdown**")
st.button("Click Me")
if st.button("Click Here"):
    st.success("Button was clicked")
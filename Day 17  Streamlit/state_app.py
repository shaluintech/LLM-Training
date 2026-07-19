import streamlit as st
count = 0
if st.button("Add one"):
    count = count + 1
st.write("Count",count)
st.session_state
if "count" not in st.session_state:
    if "count" not in st.session_state:
      st.session_state.count = 0
      st.session_state.count +=1
st.write("Count value:",st.session_state.count)
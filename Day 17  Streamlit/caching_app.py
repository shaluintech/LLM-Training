import streamlit as st
import time
st.title("Caching: Run slow work once, not every rerun")

def slow unchached(n):
    time.sleep(2)
    return n*2
@st.cache_data
def slow_cached(n):
    time.sleep(2)
    return n*2

st.header("Uncached: Slow every single time")
number1 = st.slider("Pick a number (unchached)",1,10,3)
result1 = slow_unchached(number1)
st.write(f"Result (unchached): {result1}")
if st.button("Square (unchached)"):
    result = slow_unchached(result1)
    st.success(f"{number1} sqaured is {result}")

st.divider()
st.header("Cached: Slow once per value")
number2 = st.slider("Pick a number (cached)",1,10,3)
if st.button("Square (cached)"):
    result = slow_cached(number2)
    st.success(f"{number2} sqaured is {result}")
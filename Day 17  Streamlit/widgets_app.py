import streamlit as st
st.title("Widgets: input you cam read")
st.header("Tell me about you!")
name = st.text_input("What is y0ur name?","")
age = st.slider("How old are you?",0,100,200)
city= st.selectbox("Which city?",["LKo","Delhi","Mumbai","Pune"])
st.write(f"Hi **{name or 'friend'}**,age: {age},city:{city}" )
st.divider()
st.header("Live Tip Calculator")
bill = st.number_input("Bill amount(Rs)",min_value=0.0,value=500.0,step=50.5)
tip_percent = st.slider("Tip Percentage", 0, 50, 10)
tip = bill * tip_percent/100
total = bill + tip
st.metric("Toatl to pay",f"Rs{total:.2f}")
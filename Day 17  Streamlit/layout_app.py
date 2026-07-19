import streamlit as st
st.title("Layout a Page")
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Model",["llama","OpenAI","Gemini"])
temperature = st.sidebar.slider("Temperature",0.0 , 1.0 , 0.5)
st.write(f"You picked **{model} at temp :{temperature}")
st.header("Welcome to new page")

st.header("Cols put things side by side")
col1,col2,col3=st.columns(3)
with col1:
    st.write("col 1 content")
    st.metric("user",1290,"+120")
with col2:
    st.write("col 2 content")
    st.metric("Active Today",120,"-8")
with col3:
    st.write("col 2 content")
    st.metric("Singup",57,"+15")
st.divider()
st.header("Tabs act like a mini page")
tab_summary , tab_details = st.tabs(["Summary","Details"])
with tab_summary:
    st.write("This is summary tabs")
with tab_details:
    st.write("This is details tabs")

st.header("Expander hide long or optional content")
with st.expander("Click to see content"):
    st.code("you are helpful assistant",language= "text")
show_debug = st.sidebar.checkbox("show Debug info")
if show_debug:
    st.warning("Debug mode is on")
    st.json({"mode":model,"temperature":temperature})
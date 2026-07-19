import streamlit as st
import pandas as pd
st.title("Ways to show content")
st.header("1.Text")
st.write("st.write prints plain text and supports **markdown** also")
st.code("def greet (name) return f'Hi {name}'" , language="python")
st.divider()
st.header("2. Data and Tables")
students = pd.DataFrame(
    {
        "Name": ["John", "Alice", "Bob"],
        "City": ["New York", "Los Angeles", "Chicago"],
        "Score": [85, 90, 78]

    
 
    }
)
st.dataframe(students,width="stretch")
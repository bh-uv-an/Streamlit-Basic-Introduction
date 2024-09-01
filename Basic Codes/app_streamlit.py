import streamlit as st
import pandas as pd 


# Title of the application 
st.title("Hello Streamlit")

# Display a simple text 
st.write("Just Testing")

#Creating a dataframe 
data = pd.DataFrame(
    {
        "First column" : [1,2,3,4],
        "Second column" : [10,20,90,160]
    }
)

#Displaying the dataframe 
st.write("Displaying the data")
st.write(data)

# Streamlit Basic Introduction

This repository is a quick revision guide to remember the basics of Streamlit, a powerful tool for building data science and machine learning applications.

## What is Streamlit?

Streamlit is an open-source app framework designed specifically for machine learning and data science projects. It allows you to create beautiful and interactive applications using simple Python scripts.

## Basic Example

Below is a simple example to demonstrate the basic usage of Streamlit.

### Code Example

```python
import streamlit as st
import pandas as pd

# Title of the application
st.title("Hello Streamlit")

# Display a simple text
st.write("Just Testing")

# Creating a dataframe
data = pd.DataFrame(
    {
        "First column": [1, 2, 3, 4],
        "Second column": [10, 20, 90, 160]
    }
)

# Displaying the dataframe
st.write("Displaying the data")
st.write(data)
```
### Output: 
![Screenshot 2024-09-01 091026](https://github.com/user-attachments/assets/2c8072b0-1336-4f6e-b538-d72ac8542708)

## Interactive Widgets Example

Here's an example demonstrating how to use various interactive widgets in Streamlit.

### Code Example

```python
import streamlit as st 
import pandas as pd 

# Title of the application
st.title("Streamlit Text Input")

# Asking name from the user as input 
name = st.text_input("Please enter your name ")

# Displaying the entered name
if name:
    st.write(f"Your name is {name}")
    
# Creating a slider for age selection
age = st.slider("Select Your age: ", 0, 100, 18)

# Displaying the selected age
if age:
    st.write(f"Your age is: {age}")
    
# Using a select box to choose from the following options
options = ["Html", "Css", "JavaScript", "Python", "Java"]
choice = st.selectbox("Enter Your choice", options)

if choice:
    st.write(f"Your favourite Language is {choice}")
    
# Using the upload file widget to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded file's data:", data)
```

### Output: 

![Screenshot 2024-09-01 111321](https://github.com/user-attachments/assets/47c94f73-3a8c-47a3-ac9d-c694694f1067)

![Screenshot 2024-09-01 111357](https://github.com/user-attachments/assets/753223b8-2fc2-418c-b41b-baf3bfb02504)

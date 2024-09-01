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

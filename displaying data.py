import streamlit as st
import pandas as pd
import os 

# Get the current working directory
current_directory = os.getcwd() #ensure locate the csv file
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv') #can use full path locate the csv file

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';') #df stands for dataframe

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df)#when using the dataframe function the little buttoms will show at the right corner.

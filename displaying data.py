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


import pandas as pd
import streamlit as st

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df = pd.DataFrame(data)

# Show data with Streamlit elements
st.Dataframe(df)                # Interactive table
st.data_editor(df)              # Editable table
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.Dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': 'Number = {:,.0f}'})) #format function have dictionary{}inside

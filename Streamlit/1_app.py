'''
STREAMLIT :
It is an open source library in python to make web applications of data science or machine lerning projects
It is more simple than flask and helps to create dashboard or front-end template without any prior knowledge of html/css

'''
# To execute, write 'streamlit run file_name' in terminal
import streamlit as st
import pandas as pd
import numpy as np

# Creating Title
st.title('This is the title of streamlit webframework app')
st.title('This is blue color :blue[TITLE]')   # For colors

# Writing body
st.write('Hey welcome to the webpage')  # we can write any datastructure inside this

# dataframe
data = pd.DataFrame(np.random.randint(1,10,size=(5,5)),columns=['A','B','C','D','E'])
st.write(data)

# line_chart
st.line_chart(data)



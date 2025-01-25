## Using widgets in streamlit

import streamlit as st
import pandas as pd

## Creating titles
st.title(':red[Streamlit]')
st.header('Understanding common widgets in *Streamlit*')
st.subheader('The common widgets are :')

st.markdown('# This is written by _markdown_ function')
st.markdown('## We can control the size with this')

# Slider 
st.slider('Select your age : ',0,100,18)

# Upload file
upload_file = st.file_uploader('Upload file here : ','csv',accept_multiple_files=False)
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)

# Option feature
languages = [
    "Ruby", "PHP", "Swift", "Kotlin", "Go", 
    "Rust", "R", "TypeScript", "Scala", "Perl", 
    "Shell", "HTML", "CSS", "SQL", "MATLAB"
]

choices = st.selectbox('Select a choice : ',languages)
st.write(choices)


choices = st.select_slider('select a language : ',languages)
st.write('You selected ',choices)




'''
Go to 'streamlit.io' for more information and new tools
'''
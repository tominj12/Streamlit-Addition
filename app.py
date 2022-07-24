import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Subtraction of 2 given numbers

This app will give the subtraction of two given numbers!
""")
#Get Input

st.header('User Input Parameters')

No1 = st.number_input("NO_1 ",min_value=0.0,max_value=2000000.0)
No2 = st.number_input("NO_2 ",min_value=0.0,max_value=2000000.0)
result= No1 - No2
st.subheader('Subtraction')
st.write(No1 ,' - ', No2,' = ',result)

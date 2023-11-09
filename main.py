import streamlit as st
import pandas as pd



df = pd.read_csv('ratings.csv')

df_movies = pd.read_csv('movies.csv')

st.write('end of program')

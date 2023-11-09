import streamlit as st
import pandas as pd



df = pd.read_csv('popularity_ratings.csv')


st.write(df.head(20))

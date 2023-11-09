import streamlit as st
import pandas as pd



df = pd.read_csv('popularity_ranking.csv')


st.write(df.head(20))

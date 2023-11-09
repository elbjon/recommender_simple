import streamlit as st
import pandas as pd



df = pd.read_csv('popularity_ranking.csv')


st.write(df.head(20))


option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))



st.write('You selected:', option)

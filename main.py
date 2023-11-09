import streamlit as st
import pandas as pd



df = pd.read_csv('popularity_ranking.csv')


st.write(df.head(20))


option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))

n = st.slider(
    'How many recommandations would you like to receive?',
    1, 25, 12)





st.write(f'You selected: {n} recommendations to {option}')

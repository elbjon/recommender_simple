import streamlit as st
import pandas as pd



df = pd.read_csv('popularity_ranking.csv')

from PIL import Image
#opening the image
image = Image.open('Meme7-768x766.webp')
#displaying the image on streamlit app
st.image(image, caption='Enter any caption here')





st.write(df.head(20))


option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))

n = st.slider(
    'How many recommandations would you like to receive?',
    1, 25, 12)






st.button("Give me recommendations", type="primary")
if st.button('Say hello'):
    st.write(f'You selected: {n} recommendations to {option}')
else:
    st.write('Goodbye')

st.markdown('''
    :blue[Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.] ''')

#st.write('Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.')








import streamlit as st
import pandas as pd
from PIL import Image


image = Image.open('TopMenue.png')
#displaying the image on streamlit app
st.image(image, caption='Enter any caption here')

st.set_page_config(
    page_title="World's Best Movie Recommendations",
    page_icon="📽️",
)

st.write("# Welcome to WBSflix! 📽️")

df = pd.read_csv('popularity_ranking.csv')


#opening the image
#image = Image.open('Meme7-768x766.webp')
#displaying the image on streamlit app
#st.image(image, caption='Enter any caption here')





st.write(df.head(20))


option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))

n = st.slider(
    'How many recommandations would you like to receive?',
    1, 25, 12)






if st.button("Give me recommendations", type="primary"):
    st.write(f'You selected: {n} recommendations to {option}')



st.markdown('''
    :blue[Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.] ''')

#st.write('Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.')








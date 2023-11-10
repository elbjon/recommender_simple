import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="World's Best Movie Recommendations",
    page_icon="📽️",
)

#load fake top menue bar
image = Image.open('TopMenue.png')
#displaying the image on streamlit app
st.image(image, caption='')

# user welcome
st.write("# Welcome to WBSFLIX! 📽️")



# load files
df = pd.read_csv('popularity_ranking.csv')

#url = 'https://drive.google.com/file/d/1x-YdD7anrrsnFaS5jUTfq9ELRXZ0iMQL/view?usp=sharing'
#path = 'https://drive.google.com/uc?id='+url.split('/')[-2]
movies_cosines_matrix = pd.read_csv("https://drive.google.com/u/0/uc?id=1x-YdD7anrrsnFaS5jUTfq9ELRXZ0iMQL&amp;export=download&amp;confirm=t&amp;uuid=729f37c9-a7e8-4081-8042-685d94d1b852&amp;at=AB6BwCAMtTPXBhdWE1nSBFCXloZN:1699575124612")






st.write(df.head(20))
st.write(movies_cosines_matrix.head(20))

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








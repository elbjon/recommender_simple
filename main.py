import streamlit as st
import pandas as pd
from PIL import Image
import requests

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
df = pd.read_csv('popularity_ranking_15.csv')
df1 = pd.read_csv('mcm_15_1.csv', index_col='movieId')
df2 = pd.read_csv('mcm_15_2.csv', index_col='movieId')

movies_cosines_matrix = pd.concat([df1, df2], ignore_index=False)
user_movies_matrix = pd.read_csv('umm_15.csv', index_col='userId')








## Start of App

option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))

movieId = df.loc[df['title'] == option,['movieId']].iat[0, 0] #takes the first value
url = df.loc[df['title'] == option,['posters']].iat[0, 0]


abc = st.slider(
    'How many recommendations would you like to receive?',
    1, 15, 5)






n = abc

# Button that contains the functionality to give out item based recommendations
if st.button("Give me recommendations", type="primary"):
    lovely_bones_isbn = str(int(movieId)) #dont ask why.
    movieId = str(int(movieId))
    # Create a DataFrame using the values from 'books_cosines_matrix' for the 'lovely_bones_isbn' book.
    lovely_bones_cosines_df = pd.DataFrame(movies_cosines_matrix.loc[:,movieId])
    item_cosines_df = pd.DataFrame(movies_cosines_matrix.loc[:,movieId])

    # Rename the column 'lovely_bones_isbn' to 'lovely_bones_cosine'
    lovely_bones_cosines_df = lovely_bones_cosines_df.rename(columns={lovely_bones_isbn: 'lovely_bones_cosine'})
    item_cosines_df = item_cosines_df.rename(columns={movieId: 'item_cosine'})
    
    # Remove the row with the index 'lovely_bones_isbn'
    lovely_bones_cosines_df = lovely_bones_cosines_df[lovely_bones_cosines_df.index != lovely_bones_isbn]
    st.write('70: ', lovely_bones_cosines_df.head(10))
    
    
    
    # Sort the 'lovely_bones_cosines_df' by the column 'lovely_bones_cosine' column in descending order.
    #lovely_bones_cosines_df = lovely_bones_cosines_df.sort_values(by='lovely_bones_cosine', ascending=False)

    # Find out the number of users rated both The Lovely Bones and the other book
    no_of_users_rated_both_books = [sum((user_movies_matrix[str(int(lovely_bones_isbn))] > 0) & (user_movies_matrix[str(int(isbn))] > 0)) for isbn in lovely_bones_cosines_df.index]

    # Create a column for the number of users who rated The Lovely Bones and the other book
    lovely_bones_cosines_df['users_who_rated_both_books'] = no_of_users_rated_both_books

#    # Remove recommendations that have less than 5 users who rated both books.
    lovely_bones_cosines_df = lovely_bones_cosines_df[lovely_bones_cosines_df["users_who_rated_both_books"] > 5]
 
    

    my_top_10 = (lovely_bones_cosines_df #item_correlations_df
              .reset_index()
              .merge(df.drop_duplicates(subset='movieId'),
                                         on='movieId',
                                         how='left')
                )
    my_top_10 = my_top_10.head(n)#.sort_values(by='', ascending=False).head(n)

    st.write(my_top_10[['title','mean','posters']])
    st.write(my_top_10.head(1))


# show movie poster of chosen movie
response = requests.get(url, stream=True)
img = Image.open(response.raw)
st.image(img)


st.write('<br><br><br>\n\n\n\n<br><br><br><br>')

#st.markdown('''
#    :blue[Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.] ''')










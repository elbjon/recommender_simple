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
df = pd.read_csv('popularity_ranking_15.csv')
df1 = pd.read_csv('mcm_15_1.csv', index_col='movieId')
df2 = pd.read_csv('mcm_15_2.csv', index_col='movieId')
user_movies_matrix = pd.read_csv('umm_15.csv', index_col='userId')
#url = 'https://drive.google.com/file/d/1x-YdD7anrrsnFaS5jUTfq9ELRXZ0iMQL/view?usp=sharing'
#path = 'https://drive.google.com/uc?id='+url.split('/')[-2]
#df666 = pd.read_csv("https://drive.google.com/u/0/uc?id=1x-YdD7anrrsnFaS5jUTfq9ELRXZ0iMQL&amp;export=download&amp;confirm=t&amp;uuid=729f37c9-a7e8-4081-8042-685d94d1b852&amp;at=AB6BwCAMtTPXBhdWE1nSBFCXloZN:1699575124612")

#st.write(user_movies_matrix.head())

movies_cosines_matrix = pd.concat([df1, df2], ignore_index=False)
#st.write(movies_cosines_matrix.head(-1), movies_cosines_matrix.head(-5))

## Start of App
#st.write(df.head(20))


option = st.selectbox(
    'Choose a movie!',
    df['title'].head(50))

movieId = df.loc[df['title'] == option,['movieId']].iat[0, 0] #takes the first value
st.write(movieId)

abc = st.slider(
    'How many recommendations would you like to receive?',
    1, 15, 6)



n = abc

#def myfunction(movieId, n):
if st.button("Give me recommendations", type="primary"):
    lovely_bones_isbn = str(int(movieId))
    #st.write(lovely_bones_isbn, n)
    #st.write(movies_cosines_matrix)
#    # Create a DataFrame using the values from 'books_cosines_matrix' for the 'lovely_bones_isbn' book.
    lovely_bones_cosines_df = pd.DataFrame(movies_cosines_matrix.loc[:,str(n)])
    
#
#    # Rename the column 'lovely_bones_isbn' to 'lovely_bones_cosine'
    lovely_bones_cosines_df = lovely_bones_cosines_df.rename(columns={lovely_bones_isbn: 'lovely_bones_cosine'})
#
#   # Remove the row with the index 'lovely_bones_isbn'
    lovely_bones_cosines_df = lovely_bones_cosines_df[lovely_bones_cosines_df.index != lovely_bones_isbn]
    #st.write(lovely_bones_isbn, n,lovely_bones_cosines_df)
#    # Sort the 'lovely_bones_cosines_df' by the column 'lovely_bones_cosine' column in descending order.
    lovely_bones_cosines_df = lovely_bones_cosines_df.sort_values(by=str(int(n)), ascending=False)
    #st.write('67', lovely_bones_isbn, n,lovely_bones_cosines_df)
    #st.write('68', user_movies_matrix)
#    # Find out the number of users rated both The Lovely Bones and the other book
    no_of_users_rated_both_books = [sum((user_movies_matrix[str(int(lovely_bones_isbn))] > 0) & (user_movies_matrix[str(int(isbn))] > 0)) for isbn in lovely_bones_cosines_df.index]
    #st.write('71', no_of_users_rated_both_books)
#    # Create a column for the number of users who rated The Lovely Bones and the other book
    lovely_bones_cosines_df['users_who_rated_both_books'] = no_of_users_rated_both_books
#
#    # Remove recommendations that have less than 10 users who rated both books.
#    lovely_bones_cosines_df = lovely_bones_cosines_df[lovely_bones_cosines_df["users_who_rated_both_books"] > 5]

    

    my_top_10 = (lovely_bones_cosines_df #item_correlations_df
              .head(n)
              .reset_index()
              .merge(df.drop_duplicates(subset='movieId'),
                                         on='movieId',
                                         how='left'))
    st.write(my_top_10[['title','mean']])
        








#if st.button("Give me recommendations", type="primary"):
#    st.write(f'You selected: {n} recommendations to {option}')
#    st.write(myfunction(5, 2))

import streamlit.components.v1 as components

def main():

    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

    imageUrls = [
        "https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        "https://images.unsplash.com/photo-1610016302534-6f67f1c968d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1075&q=80",
        "https://images.unsplash.com/photo-1516550893923-42d28e5677af?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=872&q=80",
        "https://images.unsplash.com/photo-1541343672885-9be56236302a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1557744813-846c28d0d0db?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1118&q=80",
        "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1595867818082-083862f3d630?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1622214366189-72b19cc61597?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1558180077-09f158c76707?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        "https://images.unsplash.com/photo-1520106212299-d99c443e4568?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1534430480872-3498386e7856?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1571317084911-8899d61cc464?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1624704765325-fd4868c9702e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
    ]
    selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

    if selectedImageUrl is not None:
        st.image(selectedImageUrl)

if __name__ == "__main__":
    main()

st.markdown('''
    :blue[Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.] ''')

#st.write('Disclaimer: This application uses TMDB and the TMDB APIs but is not endorsed, certified, or otherwise approved by TMDB.')








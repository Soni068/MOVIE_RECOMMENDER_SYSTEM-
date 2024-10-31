import pandas as pd
import requests
import streamlit as st
import pickle


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def app():
    #st.balloons()
    # Load custom CSS
    #mrs = "Movie Recommemder System"
    #st.image("https://editor.analyticsvidhya.com/uploads/76889recommender-system-for-movie-recommendation.jpg")
    div_with_background = """
    <div style="background-color: #F73718; 
    padding: 20px;
    border-radius: 25px;">
        <h1>Movie Recommemder System</h1>
        
    </div>
    """
    # Render the div using st.write()
    st.write(div_with_background, unsafe_allow_html=True)
    def recommend(movie):
        movie_index = movies[movies["title"] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies=[]
        recommended_movies_poster=[]
        for i in movies_list:
            movie_id =movies.iloc[(i[0])].movie_id

            recommended_movies.append(movies.iloc[(i[0])].title)
            recommended_movies_poster.append(fetch_poster(movie_id))
            # fetch poster from api
            #api_key = "43ad55b5005c083d95dc19259ef06293"
        return recommended_movies,recommended_movies_poster

    movie_dict = pickle.load(open('movie_dict.pkl','rb'))
    movies =pd.DataFrame(movie_dict)

    similarity =  pickle.load(open('similarity.pkl','rb'))
    #st.title(mrs)
    #text=st.write(text_color, unsafe_allow_html=True)
    suggestion = movies['title'].values;
    selected_movies_name =st.selectbox('TYPE YOUR MOVIE',suggestion)
    if st.button('Recommend'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movies_name)
        col1, col2, col3, col4, col5 =  st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])



if __name__ == "__main__":
    app()

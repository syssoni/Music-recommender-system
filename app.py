import streamlit as st
import pandas as pd
import pickle
import string


def recommend(songs):
    songs_df = pickle.load(open('song_df.pkl','rb'))
    new_new_df = songs_df.copy(deep=True)
    new_new_df['Song'] = new_new_df['Song'].str.lower()
    songs = str(songs).lower()
    t_df = new_new_df[new_new_df['Song'] == songs]
    if(len(t_df)==0):
        print("Song not found in database so can't recommend...")
        return
    song_index = new_new_df[new_new_df['Song'] == songs].index[0]
    distance = similarity[song_index]
    song_list = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_songs = []
    for i in song_list:
       recommended_songs.append(new_new_df.iloc[i[0]].Song)
    return recommended_songs

st.header("Music Recommender System",anchor= None,divider ='rainbow')

songs_list = pickle.load(open('songs_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


songs = pd.DataFrame(songs_list)

selected_song = st.selectbox('Choose a song',songs['Song'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_song)
    for i in recommendations:
        st.write(i)

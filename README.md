# Music recommender system
## About the project
---
A content-based music recommendation system that is designed to suggest 5 similar songs based on the user's input selection. The system recommends songs by comparing genres and artist names, using saved similarity scores from the song metadata. This system is built using a combination of data preprocessing, vectorization, and cosine similarity scoring to generate personalized suggestions. The interface is developed using Streamlit, offering a smooth and interactive user experience

**Project Structure** <br/>
- `Music_Recommendation_System.ipynb` – Jupyter notebook for data processing, feature engineering, and building the similarity matrix
- `app.py` – Web app built with Streamlit that allows users to select a song and get recommendations
- `environment.yaml` – Conda environment file with all required dependencies

**Machine learning pipeline**<br/>
- Feature extraction via TF-IDF or vector encodings
- Cosine similarity for ranking
- Precomputed similarity matrix for fast querying    

**About dataset** <br/>
- It is obtained from Kaggle
- It contains metadata about various songs, including their titles, artists, genres, album name, and other content-based features. This information is used to compute similarity between songs for recommendation purposes.
- It also contains columns like loudness, key, and acousticness, which have been dropped after data processing
- <img src="https://raw.githubusercontent.com/syssoni/Music-recommender-system/main/Application/model_out_1.png" alt="dataset description" width="70%">
  
**Data preprocessing, Data vectorization, Feature extraction, tf-idf, cosine similarity used for ranking, Recommender system, Streamlit**

## Requirements
---
**Dependencies for the project:**<br/>
- Python 3.10
- Pandas
- Scikit-learn
- Streamlit<br/>

(Note: All the dependencies are installed in the yaml file)<br/>

**Steps for running the file:** <br/>
1. **Clone the repository**<br/>
   git clone https://github.com/syssoni/Music-recommender-system.git<br/>
2. **Run the environment.yaml file**<br/>
  conda env create -f environment.yaml<br/>
3. **Activate the environment**<br/>
  conda activate music_rec_sys
4. **Add the required data files**<br/>
   If not yet created, run Music_Recommendation_System.ipynb to generate them.<br/>
    - songs_dict.pkl
    - song_df.pkl
    - similarity.pkl
5. **Run the streamlit app**<br/>
   streamlit run app.py
   
## Application Screenshot
---
<img src="https://raw.githubusercontent.com/syssoni/Music-recommender-system/main/Application/output_2.png" alt="Web application" width="70%">

  


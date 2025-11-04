import pandas as pd
from scipy.sparse import coo_matrix, csr_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ----------- Data Loading & Preprocessing -----------
movies = pd.read_csv(r"C:\Users\mohdq\OneDrive\Desktop\Project\movies.csv")
ratings = pd.read_csv(r"C:\Users\mohdq\OneDrive\Desktop\Project\ratings.csv")

# ----------- Feature Engineering -----------
valid_movie_ids = set(movies['movieId'].unique())
filtered_ratings = ratings[ratings['movieId'].isin(valid_movie_ids)].copy()

# Create movie ID mappings
unique_movie_ids = sorted(movies['movieId'].unique())
movie_id_to_index = {movie_id: idx for idx, movie_id in enumerate(unique_movie_ids)}
index_to_movie_id = {idx: movie_id for movie_id, idx in movie_id_to_index.items()}

# Create sparse matrix
filtered_ratings['movie_index'] = filtered_ratings['movieId'].apply(lambda x: movie_id_to_index[x])
unique_user_ids = sorted(filtered_ratings['userId'].unique())
user_id_to_index = {user_id: idx for idx, user_id in enumerate(unique_user_ids)}
filtered_ratings['user_index'] = filtered_ratings['userId'].apply(lambda x: user_id_to_index[x])

user_item_sparse = coo_matrix(
    (filtered_ratings['rating'], (filtered_ratings['user_index'], filtered_ratings['movie_index'])),
    shape=(len(unique_user_ids), len(unique_movie_ids))
).tocsr()

# ----------- Model Training -----------
knn_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=11, n_jobs=-1)
knn_model.fit(user_item_sparse.T)

# ----------- Content-Based Features -----------
movies['genres'] = movies['genres'].str.split('|')
all_genres = set(genre for sublist in movies['genres'].dropna() for genre in sublist)
for genre in all_genres:
    movies[genre] = movies['genres'].apply(lambda x: 1 if genre in x else 0)
movies['clean_title'] = movies['title'].apply(lambda x: x.split('(')[0].strip().lower().replace(":", "").replace(",", "").replace(" ", ""))

# ----------- Recommendation Functions -----------
def normalize_title(title):
    title = title.split('(')[0].strip().lower().replace(":", "").replace(",", "").replace(" ", "")
    if ',' in title:
        parts = [p.strip() for p in title.split(',')]
        if parts[-1] in ['the', 'a', 'an']:
            title = f"{parts[-1]} {', '.join(parts[:-1])}"
    return title

def get_hybrid_recommendations(movie_title, weight_cf=0.5, weight_cb=0.5):
    normalized_input = normalize_title(movie_title)
    movie_row = movies[movies['clean_title'] == normalized_input]
    if movie_row.empty: return []
    
    movie_id = movie_row['movieId'].values[0]
    movie_idx = movie_id_to_index[movie_id]
    
    # Collaborative Filtering
    distances, indices = knn_model.kneighbors(user_item_sparse.T[movie_idx].toarray().reshape(1, -1), n_neighbors=11)
    cf_scores = {index_to_movie_id[i]: 1 - d for i, d in zip(indices[0], distances[0]) if i != movie_idx}
    
    # Content-Based Filtering
    genre_matrix = movies.drop(columns=['movieId', 'title', 'clean_title', 'genres']).values
    cosine_sim = cosine_similarity(genre_matrix)
    cb_scores = {index_to_movie_id[i]: cosine_sim[movie_idx][i] for i in range(len(cosine_sim[movie_idx])) if i != movie_idx}
    
    # Combine scores
    hybrid_scores = {movie: (cf_scores.get(movie, 0)*weight_cf )+ (cb_scores.get(movie, 0)*weight_cb) 
                    for movie in set(cf_scores.keys()).union(cb_scores.keys())}
    
    return movies[movies['movieId'].isin([m[0] for m in sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:10]])]['title'].tolist()

def recommend_movies(movie_title, num_recommendations=5):
    clean_input = normalize_title(movie_title)
    movie_row = movies[movies['clean_title'] == clean_input]
    if movie_row.empty: return []
    
    genre_matrix = movies.drop(columns=['movieId', 'title', 'clean_title', 'genres']).values
    cosine_sim = cosine_similarity(genre_matrix)
    idx = movie_row.index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    return movies.iloc[[i[0] for i in sim_scores]]['title'].tolist()
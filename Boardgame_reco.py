import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


main_file_path = 'boardgames.csv' 
df_main = pd.read_csv(main_file_path)


user_file_path = 'user_ratings.csv' 
df_user = pd.read_csv(user_file_path, encoding='ISO-8859-1')  


df_main = df_main[['name', 'avgweight', 'minplayers', 'maxplayers',
                   'minplaytime', 'maxplaytime', 'boardgamemechanic_cnt']]
df_user = df_user[['name', 'rating']]

# Merge
df_user_ratings = pd.merge(df_user, df_main, on='name')

# average feature values
user_profile = df_user_ratings[['avgweight', 'minplayers', 'maxplayers',
                                'minplaytime', 'maxplaytime', 'boardgamemechanic_cnt']].mean().values.reshape(1, -1)

# cosine similarities 
other_games = df_main[~df_main['name'].isin(df_user['name'])].copy()  # Use .copy() to avoid the warning
other_game_features = other_games[['avgweight', 'minplayers', 'maxplayers',
                                   'minplaytime', 'maxplaytime', 'boardgamemechanic_cnt']].values

similarities = cosine_similarity(user_profile, other_game_features)[0]

# similarities to the DataFrame
other_games.loc[:, 'similarity'] = similarities

# top 10 recommendations
top_10_recommendations = other_games.sort_values(by='similarity', ascending=False).head(10)


print("Top 10 Recommended Games for the User:")
print(top_10_recommendations[['name', 'similarity', 'avgweight', 'minplayers',
                             'maxplayers', 'minplaytime', 'maxplaytime',
                             'boardgamemechanic_cnt']])


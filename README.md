# Board Game Recommendation System

This simple project implements a content-based recommendation system for board games. Given a dataset of board games (boardgames.csv from previous repo) and a list of games a user has already rated (another csv file), the system predicts and recommends new games that the user will likely enjoy. This system is similar in principle to Netflix's recommendation system and can be used as such.


## How It Works

1. **Data Loading:** The system loads the main board games dataset and the user's ratings.
2. **Profile Creation:** The system creates a user profile based on the average features of the games that the user has already rated.
3. **Similarity Calculation:** The system computes cosine similarity between the user's profile and other games in the dataset.
4. **Recommendation:** The user is recommended to play the top 10 games with the highest similarity scores.

- **Output:**
  - A list of the top 10 recommended board games based on the user's preferences.

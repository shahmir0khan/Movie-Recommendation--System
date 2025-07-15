# 🎬 ML-Based Content-Based Movie Recommender System

This is a **machine learning project** that builds a content-based recommender system using the **TMDB 5000 movie dataset**.

It suggests similar movies based on:
- Genres
- Cast
- Crew
- Overview
- Keywords

---

## 🧠 ML Pipeline

1. **Data Loading**  
   - `tmdb_5000_movies.csv`  
   - `tmdb_5000_credits.csv`

2. **Data Preprocessing**  
   - Convert JSON-like columns using `ast.literal_eval`  
   - Extract top genres, cast, director  
   - Remove spaces, lowercase, and collapse features

3. **Feature Engineering**  
   - Create a combined tag with genres + overview + keywords + people  
   - Apply **Porter Stemming** to normalize text  
   - Vectorize using `CountVectorizer(max_features=5000, stop_words='english')`

4. **Similarity Calculation**  
   - Use **cosine similarity** to compute movie vectors  
   - Store in `.pkl` format using `pickle`

5. **Frontend UI**  
   - Streamlit-based interactive app  
   - User selects a movie and how many similar movies to recommend

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/shahmir0khan/Movie-Recommendation--System
cd MovieRecommenderSystem

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

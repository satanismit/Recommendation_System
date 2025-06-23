
# 🎬 Movie Recommendation System

This project is a simple yet powerful movie recommendation system built using collaborative filtering with the k-Nearest Neighbors (kNN) algorithm from **scikit-learn**.

---

## 📌 Overview

The system suggests similar movies based on user ratings using a user–item matrix. It uses brute-force search to find the most similar movies using kNN.

---

## 🧠 How It Works

1. **Data Preprocessing**
   - User–movie ratings are transformed into a pivot table (`movies_pivot`).
   - The pivot is converted into a sparse matrix (`movies_sparse`) for efficient similarity computation.

2. **Model Training**
   - A `NearestNeighbors` model is trained using the sparse matrix.

3. **Recommendation**
   - When given a movie index, the model returns the top `n` most similar movies based on user rating patterns.

---

## 📁 Folder Structure

```
Recommendation_System/
├── data/
│   ├── ratings.csv
│   └── movies.csv
├── notebooks/
│   └── exploration.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── recommend.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/satanismit/Recommendation_System.git
cd Recommendation_System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Preprocess the Data

```bash
python src/preprocess.py --ratings data/ratings.csv --movies data/movies.csv --out data/movies_sparse.npz
```

### 2. Train the Model

```bash
python src/train.py --input data/movies_sparse.npz --model model.pkl
```

### 3. Get Recommendations

```bash
python src/recommend.py --model model.pkl --movie_index 237 --n_neighbors 6
```

This will return:
- **Distances**: Similarity scores (lower = more similar)
- **Indices**: Index of recommended movies

---

## ✅ Example Code

```python
from sklearn.neighbors import NearestNeighbors

model = NearestNeighbors(algorithm='brute')
model.fit(movies_sparse)

distances, suggestions = model.kneighbors(
    movies_pivot.iloc[237, :].values.reshape(1, -1),
    n_neighbors=6
)
```

---

## 📦 Requirements

- Python 3.7+
- scikit-learn
- pandas
- numpy
- scipy

Install all via:
```bash
pip install -r requirements.txt
```

---

## ✨ Features to Add

- [ ] Genre-based filtering (hybrid approach)
- [ ] User-based recommendations
- [ ] Web UI (Streamlit or Flask)
- [ ] Deployment on Hugging Face or Render

---

## 📚 References

- [scikit-learn NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html)
- MovieLens Dataset or custom rating dataset

---

## 👨‍💻 Author

**Smit** – [GitHub](https://github.com/satanismit)

---

## 📄 License

This project is open source and free to use.

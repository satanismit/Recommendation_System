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


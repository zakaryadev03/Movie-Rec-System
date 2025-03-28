# Movie Recommendation System - Preprocessed Dataset

This repository contains the cleaned and preprocessed dataset for our collaborative filtering-based movie recommendation system. Below are the details to help you get started.

---

## 🗂️ Dataset Overview

### **Cleaned Files**
1. **`cleaned_ratings.csv`**:  
   - Columns: `userId`, `movieId`, `rating`   

2. **`cleaned_movies.csv`**:  
   - Columns: `movieId`, `title`, `genres` 

### **Key Changes from Raw Data**
- Removed duplicate ratings (same user-movie pairs).  
- Filtered movies with ≤ 5 ratings and users with ≤ 2 ratings.  
- Dropped `timestamp` column (not needed for our models).  
- Aligned `movies.csv` to only include movies present in `ratings.csv`.  

---

## 🛠️ How to Use
### **1. Folder structure**
Movie-Rec-System/
├── data/
│   ├── raw/                  # Original files (excluded via .gitignore)
│   └── cleaned/              # Cleaned datasets (cleaned_ratings.csv, cleaned_movies.csv)
├── notebooks/                # Jupyter notebooks for EDA/modeling
├── scripts/
│   └── preprocess.py         # Cleaning script
└── README.md
### **2. Run the preprocess.py**
``` pip install pandas matplotlib
``` python preprocess.py
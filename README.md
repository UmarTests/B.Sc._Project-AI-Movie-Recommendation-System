# 🎬 Hybrid AI Movie Recommendation System
*Award-winning ML project for Hollywood films released before 2015*

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![Status](https://img.shields.io/badge/Academic_Grade-A-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Built With](https://img.shields.io/badge/Built%20By-Umar-lightblue)

---

## 🏆 Project Highlights

- 🥇 **Best BSc Project (Grade A)** — Selected among top 1% of cohort  
- 🎯 **2 Competition Finalist** — Showcased at:
  - Project Expo Chandigarh University 2025 (Finalist, offered direct interview by one of the judges)
  - National Science Day 2025 (Finalist)
- 🎓 Built with: Python, Streamlit, Scikit-learn, Pandas, MovieLens 20M
- 🕰️ Optimized for **films released before 2015** (when user ratings are more consistent)

---

## 📖 Overview

This hybrid movie recommender system blends both collaborative and content-based filtering to recommend relevant Hollywood films.

It was trained on over **27,000 movies** and **20 million user ratings**, using:
- 🔗 **KNN-based collaborative filtering** for taste matching
- 🧠 **TF-IDF + Cosine similarity** for genre-based similarity
- ⚖️ **Hybrid weighting** to balance both approaches

> “Particularly excels with pre-2015 classic cinema, where user behavior patterns are strongest.”

---

## 🧠 System Architecture

```mermaid
graph LR
    A[User Input] --> B(Title Matching)
    B --> C{Hybrid Engine}
    C --> D[KNN]
    C --> E[Cosine Sim]
    D --> F[Recommendations]
    E --> F
```
## 📊 Model Performance

| Metric    | Score              |
|-----------|--------------------|
| RMSE      | 0.87               |
| Coverage  | 94% (pre-2015)     |
| Diversity | 0.68               |

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/UmarTests/AI-Movie-Recommendation-System.git
cd AI-Movie-Recommendation-System
pip install -r requirements.txt
streamlit run Movei_rec_app.py
```
## 🛠 Key Features

- 🎯 Personalized suggestions using hybrid ML techniques  
- 🗃️ Trained on MovieLens 20M dataset  
- 🧩 Robust against title misspellings  
- 🖥️ Optional Streamlit UI for end-user interaction  
- 🎥 Focused on films released before 2015 for rating strength  

---

## 🎓 Academic Recognition

- 📌 Capstone Project for BSc in Computer Science  
- 🏅 Grade A and Best Project Award  
- 🏆 Finalist and awardee in multiple competitions  
- 🧠 Demonstrated core ML techniques: matrix factorization, sparse vectors, cosine distance  

---

## ✨ Why This Project Stands Out

```diff
+ Demonstrates mastery in applied ML and recommender systems  
+ Focused on pre-2015 cinema: real-world data quirks handled  
+ End-to-end ready: From notebook → deployable UI  
+ Git versioned, modular Python architecture  
```

---

## 📂 File Structure

```bash
├── Movie_Rec_proj.py           # Recommender engine logic  
├── Movei_rec_app.py            # Streamlit UI (optional)  
├── recommendation_system.py    # Core similarity functions  
├── requirements.txt            # All dependencies  
├── README.md                   # You're reading it  
```

---

## 📫 Let’s Connect

- 🔗 LinkedIn : www.linkedin.com/in/mohammad-umar-9127162b8
- 🌐 Portfolio : https://github.com/UmarTests
- 📧 umar.test.49@gmail.com 

---

## 📄 License

**MIT License** – Free to use, fork, and learn from.

> For detailed methodology and dataset processing, see the [📄 Project Report (PDF)](Project_Report_Umar_final.pdf)

---



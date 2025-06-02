# Semantic News Recommender

## Description

The Semantic News Recommender is an intelligent search application designed to improve the way users discover news articles. Unlike traditional keyword-based search engines, it leverages semantic search powered by natural language processing to understand the meaning behind user queries. Using pre-trained Sentence Transformer models, the system converts news articles and queries into vector embeddings that capture their contextual meaning.

These embeddings are stored and searched efficiently using Pinecone, a cloud-based vector database optimized for similarity search. The application features a user-friendly web interface built with Streamlit, enabling users to quickly find news articles relevant to their interests, even when their search terms differ from the article text.

This project demonstrates the power of combining modern NLP techniques and vector search to create smarter, more accurate search experiences.

---


![image](https://github.com/user-attachments/assets/1c3e1ec6-aa79-4916-9aac-971dfae0d922)


---

## Technologies Used

- **Python** — Primary programming language
- **SentenceTransformers** — For generating semantic embeddings from text
- **Pinecone** — Cloud-native vector database for efficient similarity search
- **Streamlit** — Web framework for building the interactive user interface
- **Pandas** — Data handling and preprocessing
- **NumPy** — Numerical operations on embeddings

---

## Features

- Converts news articles into semantic embeddings for context-aware search
- Uses Pinecone to perform fast and scalable similarity searches on vector data
- Accepts natural language queries and finds relevant articles based on meaning
- Displays article previews and categories in an easy-to-navigate web app
- Supports searching large news datasets with high-dimensional embeddings
- Demonstrates how to integrate NLP models, vector databases, and web apps

---

## Installation

1. **Clone the repository:**
  ```bash
  git clone https://github.com/amarkosovac11/Semantic-News-Recommender.git
  cd Semantic-News-Recommender
  ```
2. **Create a virtual environment (optional but recommended):**
  ```bash
  python -m venv venv
  source venv/bin/activate
  # On Windows use: venv\Scripts\activate
  ```
3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
4. **Run the application**
  ```bash
  streamlit run scripts/5_app.py
  ```



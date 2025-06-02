import streamlit as st
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from urllib.parse import quote, unquote
import pandas as pd
import pickle

# Load model and Pinecone
model = SentenceTransformer("all-MiniLM-L6-v2")
pc = Pinecone(api_key="pcsk_3bfZ9F_Jh7rDCAAygYJSctaYVmn3JFDheg8mNBjSHeLZRJcfL72Qi7RSPj9iQrsAs8gR1o")
index = pc.Index("news-recommender1")

# Load embeddings and articles (for local article lookup)
with open("data/embeddings.pkl", "rb") as f:
    all_articles = pickle.load(f)

# ✅ Use updated method to read query parameters
params = st.query_params
article_id = params.get("article_id", [None])[0]

if article_id is not None:
    # Show full article
    article = all_articles[int(article_id)]
    st.title("📰 Full Article")
    st.subheader(f"Category: {article['category']}")
    st.write(article["text"])
    st.markdown("[🔙 Back to search](./)")
else:
    # Normal search view
    st.title("📰 Semantic News Recommender")
    query = st.text_input("Enter your search query")

    if query:
        query_vector = model.encode(query).tolist()
        results = index.query(vector=query_vector, top_k=5, include_metadata=True)

        st.subheader("Top Matches")
        for match in results["matches"]:
            # Try to find this article in our local file (by text match)
            text = match["metadata"]["text"]
            article_id = next((i for i, art in enumerate(all_articles) if art["text"] == text), None)

            st.markdown(f"**Category:** {match['metadata']['category']}")
            st.markdown(f"{text[:400]}...")

            if article_id is not None:
                url = f"/?article_id={article_id}"
                st.markdown(f"[📰 Read full article]({url})", unsafe_allow_html=True)

            st.markdown("---")

from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Connect to Pinecone
pc = Pinecone(api_key="pcsk_3bfZ9F_Jh7rDCAAygYJSctaYVmn3JFDheg8mNBjSHeLZRJcfL72Qi7RSPj9iQrsAs8gR1o")
index = pc.Index("news-recommender1", spec=ServerlessSpec(cloud="aws", region="us-east-1"))

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Input + Query
query = input("🔍 Enter your search query: ")
query_vector = model.encode(query).tolist()

# Run search
results = index.query(vector=query_vector, top_k=5, include_metadata=True)

# Show results
for match in results["matches"]:
    print("\n---")
    print("Score:", round(match["score"], 3))
    print("Category:", match["metadata"]["category"])
    print("Text:", match["metadata"]["text"][:300], "...")

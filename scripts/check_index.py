from pinecone import Pinecone, ServerlessSpec

# Connect to Pinecone
pc = Pinecone(api_key="pcsk_3bfZ9F_Jh7rDCAAygYJSctaYVmn3JFDheg8mNBjSHeLZRJcfL72Qi7RSPj9iQrsAs8gR1o")

# Connect to index
index = pc.Index("news-recommender1", spec=ServerlessSpec(cloud="gcp", region="us-central1"))

# Show stats
stats = index.describe_index_stats()
print(stats)

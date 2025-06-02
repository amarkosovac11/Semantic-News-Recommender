import pickle
from tqdm import tqdm
from pinecone import Pinecone, ServerlessSpec

# Connect to Pinecone
pc = Pinecone(api_key="pcsk_3bfZ9F_Jh7rDCAAygYJSctaYVmn3JFDheg8mNBjSHeLZRJcfL72Qi7RSPj9iQrsAs8gR1o")

# Connect to your index (make sure it exists!)
index = pc.Index("news-recommender1", spec=ServerlessSpec(cloud="aws", region="us-east-1"))

# Load vectors
with open("data/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

# Upload in batches
batch_size = 100
for i in tqdm(range(0, len(data), batch_size)):
    batch = data[i:i+batch_size]
    ids = [str(i+j) for j in range(len(batch))]
    vectors = [(ids[j], item["embedding"], {
        "text": item["text"],
        "category": item["category"]
    }) for j, item in enumerate(batch)]
    index.upsert(vectors)

print("✅ Upload to Pinecone complete")

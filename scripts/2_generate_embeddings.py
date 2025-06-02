import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Load cleaned news data
df = pd.read_csv("data/cleaned_news.csv")

# Load MiniLM model (384-dim output)
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = []

print("🔄 Encoding articles...")
for _, row in tqdm(df.iterrows(), total=len(df)):
    try:
        text = f"{row['headline']} {row['short_description']}"
        vector = model.encode(text)  # 384-dim
        embeddings.append({
            "embedding": vector,
            "text": text,
            "category": row["category"]
        })
    except Exception as e:
        print(f"❌ Skipped row due to error: {e}")

# Save embeddings
with open("data/embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print(f"✅ Done! Saved {len(embeddings)} vectors to data/embeddings.pkl")

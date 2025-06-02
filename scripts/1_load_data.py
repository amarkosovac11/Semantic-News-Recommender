
import pandas as pd

# Load JSON file
df = pd.read_json("data/News_Category_Dataset_v3.json", lines=True)

# Combine headline and short description
df["full_text"] = df["headline"] + " " + df["short_description"]

# Drop rows with missing values
df.dropna(subset=["full_text"], inplace=True)

# Save to CSV for later use
df.to_csv("data/cleaned_news.csv", index=False)
print("✅ Data loaded and saved to cleaned_news.csv")

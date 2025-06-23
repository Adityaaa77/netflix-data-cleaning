import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Step 2: Check for null values
print("Null values before cleaning:\n", df.isnull().sum())

# Step 3: Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='mixed', errors='coerce')
df['date_added'] = df['date_added'].fillna(df['date_added'].min())
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Standardize text
df['type'] = df['type'].str.strip().str.lower()
df['country'] = df['country'].str.strip()
df['rating'] = df['rating'].str.strip().str.upper()

# Step 6: Rename columns
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Step 7: Fix data types
df['release_year'] = df['release_year'].astype(int)

# Step 8: Export cleaned data
df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaning completed. Cleaned file saved as 'netflix_cleaned.csv'.")

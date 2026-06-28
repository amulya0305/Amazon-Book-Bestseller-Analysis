import pandas as pd
import sys

sys.stdout.reconfigure(encoding="utf-8")
# ======================================
# AMAZON BESTSELLER BOOKS ANALYSIS (2026)
# ======================================

# Load Dataset
df = pd.read_csv("data/BestSeller Books of Amazon.csv")

print("=" * 60)
print("AMAZON BESTSELLER BOOKS ANALYSIS (2026)")
print("=" * 60)

# First 5 Records
print("\n1. First 5 Records")
print(df.head())

# Last 5 Records
print("\n2. Last 5 Records")
print(df.tail())

# Dataset Shape
print("\n3. Dataset Shape")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# Column Names
print("\n4. Column Names")
print(df.columns)

# Dataset Information
print("\n5. Dataset Information")
df.info()

# Missing Values
print("\n6. Missing Values")
print(df.isnull().sum())

# Duplicate Records
print("\n7. Duplicate Records")
print(df.duplicated().sum())

# Summary Statistics
print("\n8. Summary Statistics")
print(df.describe())

# Convert Price column to numeric
df["Price"] = (
    df["Price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Total Books
print("\n9. Total Books")
print(len(df))

# Number of Unique Books
print("\n10. Unique Books")
print(df["Book Name"].nunique())

# Number of Unique Authors
print("\n11. Unique Authors")
print(df["Author Name"].nunique())

# Top 10 Authors
print("\n12. Top 10 Authors")
print(df["Author Name"].value_counts().head(10))

# Highest Rated Books
print("\n13. Top 10 Highest Rated Books")
print(
    df.sort_values(by="Rating", ascending=False)[
        ["Book Name", "Author Name", "Rating"]
    ].head(10)
)

# Lowest Rated Books
print("\n14. Top 10 Lowest Rated Books")
print(
    df.sort_values(by="Rating")[
        ["Book Name", "Author Name", "Rating"]
    ].head(10)
)

# Most Expensive Books
print("\n15. Top 10 Most Expensive Books")
print(
    df.sort_values(by="Price", ascending=False)[
        ["Book Name", "Author Name", "Price"]
    ].head(10)
)

# Cheapest Books
print("\n16. Top 10 Cheapest Books")
print(
    df.sort_values(by="Price")[
        ["Book Name", "Author Name", "Price"]
    ].head(10)
)

# Average Rating
print("\n17. Average Rating")
print(round(df["Rating"].mean(), 2))

# Highest Rating
print("\n18. Highest Rating")
print(df["Rating"].max())

# Lowest Rating
print("\n19. Lowest Rating")
print(df["Rating"].min())

# Average Price
print("\n20. Average Price")
print(f"₹{round(df['Price'].mean(),2)}")

# Highest Price
print("\n21. Highest Price")
print(f"₹{df['Price'].max()}")

# Lowest Price
print("\n22. Lowest Price")
print(f"₹{df['Price'].min()}")

# Top 10 Expensive Authors (Average Price)
print("\n23. Authors with Highest Average Book Price")
print(
    df.groupby("Author Name")["Price"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

# Top Rated Authors (Average Rating)
print("\n24. Authors with Highest Average Rating")
print(
    df.groupby("Author Name")["Rating"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

import pandas as pd

# Load dataset
df = pd.read_csv("amazon_transformed.csv")

print("AMAZON BUSINESS INSIGHTS")
print("========================")

# 1. Total products
print("\n1. Total Products:", len(df))

# 2. Average rating
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
print("2. Average Rating:", round(df["rating"].mean(), 2))

# 3. Average discount
df["discount_percentage"] = pd.to_numeric(
    df["discount_percentage"].astype(str)
    .str.replace("%", "", regex=False),
    errors="coerce"
)
print("3. Average Discount (%):",
      round(df["discount_percentage"].mean(), 2))

# 4. Top 5 product categories
print("\n4. Top 5 Product Categories:")
print(df["category"].value_counts().head(5))

# 5. Top 5 highest-rated products
print("\n5. Top 5 Highest-Rated Products:")
print(
    df[["product_name", "rating"]]
    .dropna()
    .sort_values("rating", ascending=False)
    .head(5)
    .to_string(index=False)
)

# 6. Top 5 products by savings
if "savings" in df.columns:
    df["savings"] = pd.to_numeric(df["savings"], errors="coerce")
    print("\n6. Top 5 Products by Savings:")
    print(
        df[["product_name", "savings"]]
        .dropna()
        .sort_values("savings", ascending=False)
        .head(5)
        .to_string(index=False)
    )

# Save business insights report
with open("business_insights_report.txt", "w", encoding="utf-8") as f:
    f.write("AMAZON BUSINESS INSIGHTS\n")
    f.write("========================\n")
    f.write(f"Total Products: {len(df)}\n")
    f.write(f"Average Rating: {df['rating'].mean():.2f}\n")
    f.write(
        f"Average Discount: {df['discount_percentage'].mean():.2f}%\n"
    )
    f.write("\nTop 5 Product Categories:\n")
    f.write(df["category"].value_counts().head(5).to_string())

print("\nBusiness insights generated successfully!")
print("Report saved as business_insights_report.txt")

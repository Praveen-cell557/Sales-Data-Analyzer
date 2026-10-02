import pandas as pd
import numpy as np


# ==========================================
# SALES DATA ANALYZER
# ==========================================

# Load dataset
df = pd.read_csv("sales.csv")

print("===== SALES DATA ANALYZER =====")


# ==========================================
# 1. VIEW DATA
# ==========================================

print("\n1. First 5 Rows")
print(df.head())

print("\n2. Last 5 Rows")
print(df.tail())


# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\n3. Dataset Size")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n4. Column Names")
print(df.columns)


# ==========================================
# 3. DATA CLEANING CHECK
# ==========================================

print("\n5. Missing Values")
print(df.isnull().sum())

print("\n6. Duplicate Rows")
print(df.duplicated().sum())


# ==========================================
# 4. SALES STATISTICS
# ==========================================

total_sales = np.sum(df["Sales"])
average_sales = np.mean(df["Sales"])
highest_sale = np.max(df["Sales"])
lowest_sale = np.min(df["Sales"])
median_sale = np.median(df["Sales"])
standard_deviation = np.std(df["Sales"])

print("\n7. Sales Analysis")

print("Total Sales:", round(total_sales, 2))
print("Average Sale:", round(average_sales, 2))
print("Highest Sale:", round(highest_sale, 2))
print("Lowest Sale:", round(lowest_sale, 2))
print("Median Sale:", round(median_sale, 2))
print("Standard Deviation:", round(standard_deviation, 2))


# ==========================================
# 5. TOP 5 SALES
# ==========================================

print("\n8. Top 5 Sales")

top_sales = df.sort_values(
    "Sales",
    ascending=False
).head(5)

print(
    top_sales[
        ["Product Name", "Category", "Sales"]
    ]
)


# ==========================================
# 6. SALES ABOVE AVERAGE
# ==========================================

print("\n9. Sales Above Average")

above_average = df[
    df["Sales"] > average_sales
]

print(
    above_average[
        ["Product Name", "Sales"]
    ].head(10)
)


# ==========================================
# 7. SALES BY CATEGORY
# ==========================================

print("\n10. Sales by Category")

category_sales = df.groupby(
    "Category"
)["Sales"].sum()

print(category_sales)


# Best category
best_category = category_sales.idxmax()

print("\nBest Category:", best_category)


# ==========================================
# 8. SALES BY REGION
# ==========================================

print("\n11. Sales by Region")

region_sales = df.groupby(
    "Region"
)["Sales"].sum()

print(region_sales)


# Best region
best_region = region_sales.idxmax()

print("\nBest Region:", best_region)


# ==========================================
# 9. SALES BY SUB-CATEGORY
# ==========================================

print("\n12. Sales by Sub-Category")

subcategory_sales = df.groupby(
    "Sub-Category"
)["Sales"].sum()

print(subcategory_sales)


# Best sub-category
best_subcategory = subcategory_sales.idxmax()

print("\nBest Sub-Category:", best_subcategory)


# ==========================================
# 10. PRODUCT INFORMATION
# ==========================================

print("\n13. Product Information")

print(
    "Unique Products:",
    df["Product ID"].nunique()
)

print(
    "Unique Customers:",
    df["Customer ID"].nunique()
)

print(
    "Unique Orders:",
    df["Order ID"].nunique()
)


# ==========================================
# 11. MOST COMMON CATEGORY
# ==========================================

print("\n14. Most Common Category")

most_common_category = df["Category"].mode()[0]

print(most_common_category)


# ==========================================
# 12. MOST COMMON REGION
# ==========================================

print("\n15. Most Common Region")

most_common_region = df["Region"].mode()[0]

print(most_common_region)


# ==========================================
# 13. AVERAGE SALES BY CATEGORY
# ==========================================

print("\n16. Average Sale by Category")

average_category_sales = df.groupby(
    "Category"
)["Sales"].mean()

print(
    average_category_sales.round(2)
)


# ==========================================
# 14. HIGHEST SALE PRODUCT
# ==========================================

print("\n17. Highest Sale Product")

highest_sale_row = df.loc[
    df["Sales"].idxmax()
]

print(
    "Product:",
    highest_sale_row["Product Name"]
)

print(
    "Category:",
    highest_sale_row["Category"]
)

print(
    "Sale:",
    round(highest_sale_row["Sales"], 2)
)


# ==========================================
# 15. FINAL SUMMARY
# ==========================================

print("\n==========================================")
print("              FINAL SUMMARY")
print("==========================================")

print("Total Records:", len(df))

print("Total Sales:", round(total_sales, 2))

print("Average Sale:", round(average_sales, 2))

print("Total Orders:", df["Order ID"].nunique())

print("Total Customers:", df["Customer ID"].nunique())

print("Total Products:", df["Product ID"].nunique())

print("Best Category:", best_category)

print("Best Region:", best_region)

print("Best Sub-Category:", best_subcategory)

print("Most Common Category:", most_common_category)

print("Most Common Region:", most_common_region)

print("Highest Sale:", round(highest_sale, 2))

print("==========================================")

print("\n===== PROJECT COMPLETE =====")
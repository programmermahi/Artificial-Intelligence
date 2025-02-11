import pandas as pd
df = pd.read_csv("E:\8th semester\AI Lab\Lab Performance 02\sales - Sheet1 (1).csv")

print("First few rows of the dataset:")
print(df.head())

total_revenue_per_product = df.groupby("Product")["Revenue"].sum()

print("\nTotal Revenue per Product:")
print(total_revenue_per_product)
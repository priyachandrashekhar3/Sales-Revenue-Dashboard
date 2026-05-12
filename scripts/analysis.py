import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract month
df["Month"] = df["Order Date"].dt.month_name()

# =========================
# KPI REPORT
# =========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)

print("\n===== KPI REPORT =====")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# =========================
# SALES BY PRODUCT
# =========================

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=product_sales.index,
    y=product_sales.values
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()

# Save chart
plt.savefig("../outputs/product_sales_chart.png")

# Close figure
plt.close()

# =========================
# MONTHLY SALES TREND
# =========================

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

plt.figure(figsize=(12, 5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig("../outputs/monthly_sales_trend.png")

# Close figure
plt.close()

# =========================
# SALES BY REGION
# =========================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

# Save chart
plt.savefig("../outputs/region_sales_chart.png")

# Close figure
plt.close()

print("\nCharts saved successfully in outputs folder!")
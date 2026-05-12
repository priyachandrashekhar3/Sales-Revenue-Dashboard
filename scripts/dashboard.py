import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("../data/sales_data.csv")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract month
df["Month"] = df["Order Date"].dt.month_name()

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("Filters")

region_options = df["Region"].dropna().unique().tolist()

selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=region_options,
    default=region_options
)

product_options = df["Product"].dropna().unique().tolist()

selected_products = st.sidebar.multiselect(
    "Select Product",
    options=product_options,
    default=product_options
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(selected_regions)) &
    (df["Product"].isin(selected_products))
]

# =========================
# DASHBOARD TITLE
# =========================

st.title("Sales & Revenue Analysis Dashboard")

st.markdown(
    "Interactive dashboard for analyzing sales, revenue, and business performance."
)

# =========================
# KPI SECTION
# =========================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = len(filtered_df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

# =========================
# SALES BY PRODUCT
# =========================

st.subheader("Sales by Product")

product_sales = (
    filtered_df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots(figsize=(8, 4))

sns.barplot(
    x=product_sales.index,
    y=product_sales.values,
    ax=ax1
)

ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

st.pyplot(fig1)

# =========================
# TOP PRODUCT
# =========================

top_product = product_sales.idxmax()

st.success(f"Top Selling Product: {top_product}")

# =========================
# MONTHLY SALES TREND
# =========================

st.subheader("Monthly Revenue Trend")

monthly_sales = (
    filtered_df.groupby("Month")["Sales"]
    .sum()
)

fig2, ax2 = plt.subplots(figsize=(10, 4))

monthly_sales.plot(
    kind="line",
    marker="o",
    ax=ax2
)

ax2.set_xlabel("Month")
ax2.set_ylabel("Sales")

st.pyplot(fig2)

# =========================
# SALES BY REGION
# =========================

st.subheader("Sales by Region")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
)

fig3, ax3 = plt.subplots(figsize=(6, 4))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values,
    ax=ax3
)

ax3.set_xlabel("Region")
ax3.set_ylabel("Sales")

st.pyplot(fig3)

# =========================
# CATEGORY DISTRIBUTION
# =========================

st.subheader("Sales Distribution by Category")

category_sales = (
    filtered_df.groupby("Category")["Sales"]
    .sum()
)

fig4, ax4 = plt.subplots(figsize=(6, 6))

ax4.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%'
)

st.pyplot(fig4)

# =========================
# DOWNLOAD FILTERED DATA
# =========================

st.subheader("Download Filtered Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# =========================
# FOOTER
# =========================

st.markdown("---")
st.markdown(
    "Sales & Revenue Dashboard built using Streamlit, Pandas, Matplotlib, and Seaborn."
)
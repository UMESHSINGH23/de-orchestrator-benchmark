import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    # -------------------------------------------------
    # Create output folders
    # -------------------------------------------------
    os.makedirs("figures", exist_ok=True)
    os.makedirs("tables", exist_ok=True)

    # -------------------------------------------------
    # Load real dataset
    # -------------------------------------------------
    data_path = "data/sample/pakistan_data.csv"
    df = pd.read_csv(data_path, low_memory=False)

    # -------------------------------------------------
    # Normalize column names
    # -------------------------------------------------
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # -------------------------------------------------
    # Explicit column mapping (based on actual dataset)
    # -------------------------------------------------
    column_mapping = {
        "increment_id": "order_id",
        "customer_id": "customer_id",
        "category_name_1": "category",
        "created_at": "order_date",
        "grand_total": "sales",
        "qty_ordered": "quantity"
    }

    df.rename(columns=column_mapping, inplace=True)

    # -------------------------------------------------
    # Required columns check
    # -------------------------------------------------
    required_columns = ["order_id", "customer_id", "category", "order_date", "sales"]
    missing = [c for c in required_columns if c not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}\n"
            f"Available columns: {list(df.columns)}"
        )

    # -------------------------------------------------
    # Data cleaning
    # -------------------------------------------------
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

    df = df.dropna(subset=["order_date", "sales", "category", "customer_id"])

    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    # =================================================
    # RQ1: Average Order Value by Category
    # =================================================
    rq1 = df.groupby("category").agg(
        total_orders=("order_id", "nunique"),
        total_revenue=("sales", "sum")
    ).reset_index()

    rq1["average_order_value"] = rq1["total_revenue"] / rq1["total_orders"]
    rq1.to_excel("tables/RQ1_Table1_Average_Order_Value_By_Category.xlsx", index=False)

    plt.figure()
    plt.bar(rq1["category"], rq1["average_order_value"])
    plt.title("Average Order Value by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Order Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("figures/RQ1_Fig1_Average_Order_Value_By_Category.pdf")
    plt.close()

    # =================================================
    # RQ2: Seasonal Sales Trend
    # =================================================
    rq2 = df.groupby("month")["sales"].sum().reset_index()
    rq2.to_excel("tables/RQ2_Table1_Monthly_Sales_Summary.xlsx", index=False)

    plt.figure()
    plt.plot(rq2["month"], rq2["sales"], marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("figures/RQ2_Fig1_Monthly_Sales_Trend.pdf")
    plt.close()

    # =================================================
    # RQ3: Customer Revenue Concentration
    # =================================================
    rq3 = df.groupby("customer_id")["sales"].sum().reset_index()
    rq3 = rq3.sort_values(by="sales", ascending=False)

    rq3["cum_revenue_pct"] = rq3["sales"].cumsum() / rq3["sales"].sum() * 100
    rq3.to_excel("tables/RQ3_Table1_Customer_Revenue_Contribution.xlsx", index=False)

    plt.figure()
    plt.plot(range(1, len(rq3) + 1), rq3["cum_revenue_pct"], marker="o")
    plt.title("Revenue Concentration by Customer")
    plt.xlabel("Customers (sorted)")
    plt.ylabel("Cumulative Revenue (%)")
    plt.tight_layout()
    plt.savefig("figures/RQ3_Fig1_Revenue_Concentration_By_Customers.pdf")
    plt.close()

    # =================================================
    # RQ4: Revenue Distribution by Category
    # =================================================
    rq4 = df.groupby("category")["sales"].sum().reset_index()
    rq4.to_excel("tables/RQ4_Table1_Revenue_Distribution_By_Category.xlsx", index=False)

    plt.figure()
    plt.pie(rq4["sales"], labels=rq4["category"], autopct="%1.1f%%")
    plt.title("Revenue Distribution by Category")
    plt.tight_layout()
    plt.savefig("figures/RQ4_Fig1_Revenue_Distribution_By_Category.pdf")
    plt.close()

    # =================================================
    # RQ5: High Volume vs Low Revenue Categories
    # =================================================
    rq5 = df.groupby("category").agg(
        order_volume=("order_id", "nunique"),
        total_revenue=("sales", "sum")
    ).reset_index()

    rq5.to_excel("tables/RQ5_Table1_High_Volume_Low_Revenue_Categories.xlsx", index=False)

    plt.figure()
    plt.scatter(rq5["order_volume"], rq5["total_revenue"])
    for i, cat in enumerate(rq5["category"]):
        plt.annotate(cat, (rq5["order_volume"][i], rq5["total_revenue"][i]))
    plt.title("Order Volume vs Revenue by Category")
    plt.xlabel("Order Volume")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.savefig("figures/RQ5_Fig1_Volume_vs_Revenue_By_Category.pdf")
    plt.close()

if __name__ == "__main__":
    main()
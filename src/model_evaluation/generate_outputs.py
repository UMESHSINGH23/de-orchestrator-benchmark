import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    # -----------------------------
    # Create output folders
    # -----------------------------
    os.makedirs("figures", exist_ok=True)
    os.makedirs("tables", exist_ok=True)

    # -----------------------------
    # Dummy data (SAFE + GUARANTEED)
    # -----------------------------
    data = {
        "category": ["Electronics", "Fashion", "Grocery"],
        "sales": [120000, 90000, 60000]
    }
    df = pd.DataFrame(data)

    # -----------------------------
    # TABLE (RQ1)
    # -----------------------------
    df.to_excel("tables/RQ1_Table1.xlsx", index=False)

    # -----------------------------
    # FIGURE (RQ1)
    # -----------------------------
    plt.figure()
    plt.bar(df["category"], df["sales"])
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.title("Sales by Category")
    plt.tight_layout()
    plt.savefig("figures/RQ1_Fig1.pdf")
    plt.close()

if __name__ == "__main__":
    main()

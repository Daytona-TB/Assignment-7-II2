import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- Set your local path here ----
# Replace with the actual path to your CSV file
folder = os.path.expanduser("/Users/lucashandlon/Downloads")  # or any folder where your CSV is saved
filename = "LoanDataset - LoansDatasest.csv"
filepath = os.path.join(folder, filename)

# Load the dataset
with open(filepath, "r", encoding="utf-8") as file:
    loan_df = pd.read_csv(file)

# Clean and preprocess
loan_df["loan_amnt"] = loan_df["loan_amnt"].replace('[£,]', '', regex=True).astype(float)
loan_df["customer_income"] = loan_df["customer_income"].replace('[£,]', '', regex=True)
loan_df["customer_income"] = pd.to_numeric(loan_df["customer_income"], errors="coerce")

# Drop rows with nulls in key columns
loan_clean = loan_df.dropna(subset=["loan_amnt", "customer_income", "loan_int_rate", "Current_loan_status", "loan_intent", "loan_grade"])

# Standardize loan status
loan_clean["Current_loan_status"] = loan_clean["Current_loan_status"].str.upper().str.strip()
loan_clean = loan_clean[np.isfinite(loan_clean["customer_income"])]

# Zoom in by trimming extreme values
loan_clean = loan_clean[
    (loan_clean["loan_amnt"] <= loan_clean["loan_amnt"].quantile(0.95)) &
    (loan_clean["customer_income"] <= loan_clean["customer_income"].quantile(0.95)) &
    (loan_clean["loan_int_rate"] <= loan_clean["loan_int_rate"].quantile(0.95))
]

# ---- Visualization 1: Loan Amount by Grade and Status ----
plt.figure(figsize=(12, 6))
grades = sorted(loan_clean["loan_grade"].unique())
statuses = ["DEFAULT", "NO DEFAULT"]

box_data = []
box_positions = []
labels = []
current_pos = 1

for grade in grades:
    for status in statuses:
        data = loan_clean[(loan_clean["loan_grade"] == grade) & (loan_clean["Current_loan_status"] == status)]["loan_amnt"]
        box_data.append(data)
        box_positions.append(current_pos)
        labels.append(f"{grade}\n{status}")
        current_pos += 1

plt.boxplot(box_data, positions=box_positions, patch_artist=True)
plt.xticks(box_positions, labels, rotation=45)
plt.title("Loan Amount by Grade and Loan Status")
plt.ylabel("Loan Amount (£)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- Visualization 2: Interest Rate by Loan Intent ----
plt.figure(figsize=(12, 6))
intents = sorted(loan_clean["loan_intent"].unique())
intent_data = [loan_clean[loan_clean["loan_intent"] == intent]["loan_int_rate"] for intent in intents]

plt.boxplot(intent_data, labels=intents, patch_artist=True)
plt.title("Interest Rate Distribution by Loan Intent")
plt.ylabel("Interest Rate (%)")
plt.xticks(rotation=30)
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- Visualization 3: Income Histogram by Loan Status ----
plt.figure(figsize=(10, 6))
bins = np.linspace(loan_clean["customer_income"].min(), loan_clean["customer_income"].max(), 30)

for status in statuses:
    subset = loan_clean[loan_clean["Current_loan_status"] == status]
    plt.hist(subset["customer_income"], bins=bins, alpha=0.6, label=status, edgecolor='black')

plt.title("Income Distribution by Loan Status")
plt.xlabel("Customer Income (£)")
plt.ylabel("Number of Customers")
plt.legend(title="Loan Status")
plt.grid(True)
plt.tight_layout()
plt.show()

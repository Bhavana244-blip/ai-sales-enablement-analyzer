import sys
import os

sys.path.append(os.path.dirname(__file__))

from data_loader import load_and_prepare_data
from scorer import score_lead

df = load_and_prepare_data("data/sales_pipeline.xlsx")

print("\n=== LEAD SCORES ===\n")

for _, row in df.iterrows():
    result = score_lead(row)
    print(
        row["lead_id"],
        row["company"],
        "→",
        result["score"],
        "|",
        result["category"]
    )
    print("Reasons:", result["reasons"])
    print("Risks:", result["risks"])
    print("-" * 40)

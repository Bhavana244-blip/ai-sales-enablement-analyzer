import pandas as pd

def load_and_prepare_data(file_path: str) -> pd.DataFrame:
   
    df = pd.read_excel(file_path)

   
    df = df.reset_index(drop=True)
    df["lead_id"] = df.index.map(lambda x: f"L{str(x+1).zfill(3)}")

    
    df = df.rename(columns={
        "Customer": "company",
        "Country": "industry",
        "Deal size": "deal_size",
        "Sales stage": "sales_stage",
        "Probability": "probability",
        "Next Steps": "call_notes"
    })

    
    def map_budget(value):
        if value < 2000:
            return "Low"
        elif value < 4000:
            return "Medium"
        return "High"

    df["budget"] = df["deal_size"].apply(map_budget)

    
    def map_urgency(stage):
        stage = str(stage).lower()
        if stage in ["identified"]:
            return "Low"
        elif stage in ["validated", "qualified"]:
            return "Medium"
        return "High"

    df["urgency"] = df["sales_stage"].apply(map_urgency)

    
    df["decision_maker_engaged"] = df["probability"].apply(
        lambda p: "Yes" if p >= 70 else "No"
    )

    final_df = df[
        [
            "lead_id",
            "company",
            "industry",
            "budget",
            "urgency",
            "decision_maker_engaged",
            "call_notes",
        ]
    ]

    return final_df

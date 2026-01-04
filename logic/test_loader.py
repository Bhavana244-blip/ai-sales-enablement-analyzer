from data_loader import load_and_prepare_data

df = load_and_prepare_data("data/sales_pipeline.xlsx")
print(df.head())


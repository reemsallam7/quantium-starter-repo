import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

df["product"] = df["product"].astype(str).str.strip()

df = df[df["product"].str.lower() == "pink morsel"]

df["price"] = df["price"].str.replace("$", "", regex=False)
df["price"] = pd.to_numeric(df["price"])

df["quantity"] = pd.to_numeric(df["quantity"])

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv("output.csv", index=False)
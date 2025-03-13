import pandas as pd 
df1= pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3= pd.read_csv("data/daily_sales_data_2.csv")

df= pd.concat([df1,df2,df3])

df= df[df["product"]=="pink morsel"]

df["price"]=df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"]=df["quantity"]*df["price"]

df=df[["sales","date","region"]]


df.to_csv("processed.csv", index=False)


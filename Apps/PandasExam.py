"""
Exercise
Load the csv from https://support.spatialkey.com/wp-content/uploads/2021/02/SalesJan2009.csv in pandas and show the last 10 records on the screen and the name of the columns that the file has
Calculate the elapsed time in hours between the Account_Created date and Last_Login
Calculate the number of transactions made by means of payment (Payment_Type)
Calculate which was the most sold product
Calculate which was the country, state and city that had the most sales (The 3 calculations separately)
Concatenate a String in a new column with:
first 2 letters of the country
First 2 letters of the state
First 2 letters of the city
a dash
First letter of the payment type
"""

import pandas as pd

link= "https://support.spatialkey.com/wp-content/uploads/2021/02/SalesJan2009.csv"

df= pd.read_csv(link)

print(df.tail(10))
print(pd.to_datetime(df["Account_Created"])-pd.to_datetime(df["Last_Login"]))

df.Payment_Type.value_counts()

df.Product.value_counts()
df.groupby(["Country", "State","City"]).size()
df.groupby(["Country", "State"]).size()
df.groupby(["Country"]).size()

#df.apply(lambda x: x["Country"][0:1]+x["State"][0:1]+x["City"][0:1], axis=1)
df["Nueva columna"]=df.apply(lambda x: (x["Country"][0:2]+x["City"][0:2]+str(x["State"])+"-"+x["Payment_Type"][0]).upper(),axis=1)
print(df.head())
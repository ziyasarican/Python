# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 00:59:45 2022

@author: ZIYA
"""
import pandas as pd

df = pd.read_csv(r"C:\Users\ZIYA\Desktop\Python Deneme\Pandas\imdb_top_1000.csv")

result = df
print (result)
print("********") 

#get first 5 records
result = df.head()
print (result)
print("********")

#get last 10 records
result = df.tail(10)
print (result)
print("********")

#get "Series_Title" column
result = df["Series_Title"]
print (result)
print("********")

#get first 10 records with "Series_Title" column
result = df["Series_Title"].head()
print (result)
print("********")

#get last 10 records "Series_Title" and "IMDB_Rating" columns
result = df[["Series_Title","IMDB_Rating"]].tail(10)
print (result)
print("********")

#get first 40 records "Series_Title" and "IMDB_Rating" columns with IMDB Rating bigger than 8.
result = df["IMDB_Rating"]>8
result = df[["Series_Title","IMDB_Rating"]].head(40)
print (result)
print("********")

#get "Series_Title" column with "Released_Year"=1991
result = df["Released_Year"]=1991
result = df[["Series_Title","Released_Year"]].head()
print (result)





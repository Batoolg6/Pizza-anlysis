# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 15:25:09 2025

@author: USER
"""

#1
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import LabelEncoder

#2
df = pd.read_excel(r"C:\Users\USER\Downloads\Data Model - Pizza Sales.xlsx")


#3
st.title("Pizza Analysis")
st.header("Pizza") # 

st.write(df) # all tha data 
st.header("state Nominal")
st.write(df.describe()) # state nominal  
st.header("State string")
st.write(df.describe(include = "object")) # state str
st.header("Missing Values")
st.write(df.isnull(). sum()) # missing value
#4

df = df.fillna({
    "unit_price":df["unit_price"].mean(),# معالجة
    "quantity":df["quantity"].median()
    })
df = df.dropna() # حذف صفوف التي لا زالت تحتوي قيم فارغة

#5 TOP products
st.header("Best Top product")
df["Total"] = df["quantity"]*df["unit_price"] # new column
top_prd = df.groupby("pizza_name")["Total"]. sum(). sort_values(ascending = False).head(10) # ترتيب تنازلي واخذ افضل 10
st.write(top_prd)
#6 رسم افضل 10 منتجات

fig , ax = plt.subplots(figsize = (10,5))
sns.barplot(x= top_prd.index,
y = top_prd.values, ax = ax)
plt.xticks(rotation = 45)
plt.title("Top 10 Best")
plt.ylabel("Total sales")
st.pyplot(fig) 


#7 Encoding (from string to int)

st.header("Data Encoding")
if "pizza_name" in df.columns:
   le = LabelEncoder()
   df["Product_encoded"] = le.fit_transform(df["pizza_name"])
   st.write("Encoding")
   st.write(df[["pizza_name","Product_encoded"]].head()) # first 5 rows
   
#8 ملخص 

st.header("Overall presentation")
st.write(f"{df['Total']. sum() :,.2f}") # توتال المبيعات
st.write(f"{df['unit_price'].mean() :,.2f}") # متوسط السعر
st.write(f"{top_prd.index[0]}") # افضل منتج

#9 

st.header("GUI")
if "pizza_name" in df.columns:
    prd_choice = st.selectbox("Pizza_Name:",df["pizza_name"].unique()) # اختيار نوع بيتزا
    filtered = df[df["pizza_name"] == prd_choice] # فلترة
    st.write(f"{prd_choice}:{filtered["Total"] . sum():,.2f}") # مجموع مبيعات
    st.bar_chart(filtered.groupby("quantity") 
                 ["Total"]. sum())





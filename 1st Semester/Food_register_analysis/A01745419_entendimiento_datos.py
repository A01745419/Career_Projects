# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:15:19 2020

@author: jlms3
"""
# José Luis Madrigal 
# A01745419
import pandas as pd
from matplotlib import pyplot as plt
doc = pd.read_excel("A01745419_comidas.xlsx", sheet_name="Sheet1")
doc.drop(doc.columns[0:3], axis=1, inplace=True)
print(doc)

plt.style.use("fivethirtyeight")
plt.hist(doc["Calorias (kcal)"], color = "orange", edgecolor = "black", bins=15)
plt.title("Calorias (kcal)")
plt.show()

plt.style.use("fivethirtyeight")
plt.hist(doc["Carbohidratos (g)"], color = "blue", edgecolor = "black", bins=15)
plt.title("Carbohidratos (g)")
plt.show()

plt.style.use("fivethirtyeight")
plt.hist(doc["Lípidos (g)"], color = "red", edgecolor = "black", bins=15)
plt.title("Lípidos (g)")
plt.show()

plt.style.use("fivethirtyeight")
plt.hist(doc["Proteína (g)"], color = "green", edgecolor = "black", bins=15)
plt.title("Proteínas (g)")
plt.show()

plt.style.use("fivethirtyeight")
plt.hist(doc["Sodio (mg)"], color = "purple", edgecolor = "black", bins=15)
plt.title("Sodio (mg)")
plt.show()

plt.style.use("fivethirtyeight")
plt.scatter(doc["Carbohidratos (g)"], doc["Calorias (kcal)"], color = "yellow", edgecolor = "black")
plt.title("Carbohidratos vs Calorias")
plt.xlabel("Carbohidratos")
plt.ylabel("Calorias")
plt.show()

import pandas as pd

wine_reviews=pd.read_csv("C:/Users/ajitn/Documents/Visual Studio Code/Pandas Course/winemag-data-130k-v2.csv",index_col=0)

print(wine_reviews.head())
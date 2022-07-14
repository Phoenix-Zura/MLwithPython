
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
df.head()
#print(df.head())
#print(df.head(10)) prints first 10 rows
df.tail()
#print(df.tail()) prints last 5 data points
#df.shape()

#print(df.shape()) prints rows*columns of the total size of the data frame
#df.size()
#print(df.size()) prints the size of the data frame
#df.len()

#print(df.len()) prints the number of rows in the columns.

#print(df.columns) prints the header of the columes if it exists

#h = df['Hired']
#print(h)
#h = df['Hired'][:5]
#print(h)

#n = df[['Years Experience','Hired']]
#print(n)

#print(df.sort_values(['Years Experience']))

degree_counts = df['Level of Education'].value_counts()
degree_counts.plot(kind='bar')


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("USA_Housing.csv")

print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)

sb.pairplot(df.select_dtypes(include=[np.number]))
plt.savefig('pairplot.png')

sb.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True)
plt.savefig('heatmap.png')

print("Plots saved as pairplot.png and heatmap.png")
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = pd.read_csv('penguins_size.csv')

print(df.head(10))

print(df.shape)

print(df.tail())

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)

print(df.describe(include= 'all'))

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True) , annot =True)
plt.savefig('capstone_heatmap.png')
plt.close()

df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.savefig('capstone_hist.png')
plt.close()

df.select_dtypes(include=[np.number]).plot(kind = "box", subplots=True, layout = (3,2) ,
 sharex=False , sharey= False , figsize = (8,12) )
plt.savefig('capstone_boxplot.png')
plt.close()

print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())

sns.countplot(data = df, x = "sex")
plt.savefig('capstone_countplot_sex.png')
plt.close()

sns.countplot(data = df, x = "island")
plt.savefig('capstone_countplot_island.png')
plt.close()

sns.countplot(data = df, x = "species")
plt.savefig('capstone_countplot_species.png')
plt.close()


sns.countplot(data = df, x = "sex",  hue ="species")
plt.savefig('capstone_countplot_sex_species.png')
plt.close()

sns.countplot(data = df, x = "island",  hue ="species")
plt.savefig('capstone_countplot_island_species.png')
plt.close()

sns.countplot(data = df, x = "island",  hue ="sex")
plt.savefig('capstone_countplot_island_sex.png')
plt.close()

sns.pairplot(data = df, hue = "species")
plt.savefig('capstone_pairplot.png')
plt.close()

print("Capstone plots saved as capstone_*.png")



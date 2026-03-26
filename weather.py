import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "ticks")

weather = pd.read_csv("Weather.csv")
weather.columns = weather.columns.str.lower()

print(weather.head())
weather.info()

sns.barplot(x = weather['humidity'], y = weather['temperature'])

sns.displot(weather['humidity'])
plt.show()


sns.displot(weather['humidity'] , kde = False, rug = True)
plt.show()

sns.jointplot(x = weather['humidity'], y = weather['temperature'])
plt.show()

sns.jointplot(x = weather['humidity'], y = weather['temperature'], kind= 'hex' )
plt.show()

sns.jointplot(x = weather['humidity'], y = weather['temperature'], kind= 'kde' )
plt.show()

sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()

sns.stripplot(x = weather['weather_type'], y = weather['temperature'])
plt.show()

sns.stripplot(x = weather['weather_type'], y = weather['temperature'], jitter=True)
plt.show()

sns.swarmplot(x = weather['humidity'], y = weather['temperature'])
plt.show()

sns.pointplot(x = weather['weather_type'], y = weather['temperature'], hue = weather['weather_type'])
plt.show()



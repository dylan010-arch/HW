#1
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid") 
sns.set_palette("pastel")

tips = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.show()

#2
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

flights_pivot = flights.pivot_table(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 8)) 
sns.heatmap(flights_pivot.corr(), annot=True, cmap="coolwarm", linewidths=.5)

plt.title("Correlation Heatmap of Monthly Passengers")

plt.show()

#3
import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")

palette = "pastel"  

plt.figure(figsize=(10, 6))  
sns.boxplot(x="cut", y="price", data=diamonds, palette=palette)

plt.title("Boxplot of Price by Cut Quality")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")

# Group the dataset by location and calculate the mean of price
df_grouped = df.groupby("LOCATION")["Price"].mean()

# Bar chart
g = sns.barplot(y=df_grouped.index, x=df_grouped.values, hue=df_grouped.index, legend=False, palette="rocket")
g.set_title('Average Price of a House by City in New York State', fontdict={'size': 15, 'weight': 'bold'})
g.set_xlabel("Average Price (in dollars)", fontdict={'size': 10})
g.set_ylabel("none", fontdict={'size': 0})
g.set(yticklabels=["Albany", "Rochester", "Syracuse", "Buffalo", "NYC"])
plt.show()

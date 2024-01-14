import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")
df["Square_Footage"] = df["Square_Footage"] * 100

# Strip plot
g = sns.stripplot(x="Price", y="LOCATION", data=df, jitter=True, hue="LOCATION", legend=False, palette="Set1")
g.set_title("House Prices in New York State", fontdict={'size': 15, 'weight': 'bold'})
g.set_xlabel("Price (in dollars)", labelpad=-0.05, fontdict={'size': 10})
g.set_ylabel("City", labelpad=0.1, fontdict={'size': 0})
g.set(yticklabels=["Albany", "Rochester", "Syracuse", "Buffalo", "NYC"])

plt.show()

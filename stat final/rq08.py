import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")
df.rename(columns={"Renovation_Cost": "Renovation Cost"}, inplace=True)
df["Square_Footage"] = df["Square_Footage"] * 100

# Bubble plot
g = sns.scatterplot(data=df, y="Square_Footage", x="Price", size="Renovation Cost", hue="LOCATION", palette="rocket", sizes=(100, 1000))
#g.set(yticklabels=["Albany", "Rochester", "Syracuse", "Buffalo", "NYC"])
g.set_xlabel("Price")
g.set_ylabel("Square Footage")
g.set_title("Price, Renovation Cost and Square Footage", fontdict={'size': 15, 'weight': 'bold'})
g.set_xticklabels(g.get_xticklabels(), rotation=0)
plt.legend(fontsize='small')
plt.show()


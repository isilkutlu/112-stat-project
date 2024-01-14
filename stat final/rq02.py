import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")
df["Square_Footage"] = df["Square_Footage"] * 100
order = ["Large", "Medium", "Small"]

# Strip plot
g = sns.stripplot(x="Square_Footage", y="Garden_Size", data=df, hue="Square_Footage", legend=False, palette="rocket", order=order)
g.set_title("Relationship between Square Footage and Garden Size", fontdict={'size': 15, 'weight': 'bold'})
g.set_xlabel("Square Footage", labelpad=-0.05, fontdict={'size': 10})
g.set_ylabel("Garden Size", labelpad=0.1, fontdict={'size': 10})
plt.show()

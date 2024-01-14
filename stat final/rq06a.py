import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")

# Calculate the house age
df["House_Age"] = (2024 - df["Year_Built"]) + (1 - df["MONTH BUILT"]) / 12

# Group the dataset by location and house age, then count the number of houses for each group
df_grouped = df.groupby(["LOCATION", "House_Age"])["House_ID"].count().reset_index()

# Scatter plot
g = sns.boxplot(x="House_Age", y="LOCATION", data=df_grouped, hue="LOCATION", palette="Set2", legend=False)
g.set_title("House Age by City", fontdict={'size': 15, 'weight': 'bold'})
g.set_xlabel("House Age (in years)", labelpad=0.5, fontdict={'size': 10})
g.set(yticklabels=["Albany", "Buffalo", "NYC", "Rochester", "Syracuse"])
plt.show()



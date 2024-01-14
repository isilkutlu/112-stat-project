import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")

# Calculate the house age
df["House_Age"] = (2024 - df["Year_Built"]) + (1 - df["MONTH BUILT"]) / 12

# Scatter plot
g = sns.scatterplot(x="House_Age", y="Price", data=df, hue="House_Age", size="Price", legend=False)
g.set_title("Relationship between House Age and Price", fontdict={'size': 15, 'weight': 'bold'})

# Regression line
h = sns.regplot(x="House_Age", y="Price", data=df, color=".3", scatter=False)
h.set_xlabel("House Age (in years)", fontdict={'size': 10})
h.set_ylabel("Price (in dollars)", labelpad=0.5, fontdict={'size': 10})
plt.show()

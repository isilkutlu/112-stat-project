import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")

# Filter the dataset to include only New York City
df_nyc = df[df["LOCATION"] == "New York City"]

# Group the dataset by house type and calculate the mean of renovation cost
df_nyc_grouped = df_nyc.groupby("HOUSE TYPE")["Renovation_Cost"].mean()

# Bar chart
g = sns.barplot(x=df_nyc_grouped.index, y=df_nyc_grouped.values, hue=df_nyc_grouped.index, legend=False, palette="rocket")
g.set_title('Renovation Cost by House Type in NYC', fontdict={'size': 15, 'weight': 'bold'})
g.set_xlabel("House Type", fontdict={'size': 10})
g.set_ylabel("Renovation Cost", fontdict={'size': 10})
g.set(xticklabels=["Apartment", "Townhouse"])
plt.show()

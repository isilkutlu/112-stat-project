import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")

# Scatter plot
g = sns.stripplot(data=df, x="Renovation_Cost", y="Price", hue="LOCATION")
g.set_ylabel("Average Renovation Cost (in dollars)", fontdict={'size': 10})
g.set_xlabel("Average Price (in dollars)" , labelpad=1, fontdict={'size': 10})
g.set_title("Renovation Cost and House Price by Location", fontdict={'size': 15, 'weight': 'bold'})
plt.show()

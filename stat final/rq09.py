import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")

# Read the dataset from Excel file
df = pd.read_excel("House_Price_temiz.xlsx")
df['Garden_Size'].replace(['Small', 'Medium', 'Large'], [1, 2, 3], inplace=True)
df.rename(columns={"Num_Bedrooms": "Number of Bedrooms", "Num_Bathrooms": "Number of Bathrooms", "Garden_Size": "Garden Size", "Square_Footage": "Square Footage", "Renovation_Cost": "Renovation Cost", "Year_Built":"Year Built"}, inplace=True)

# Pair plot
g = sns.pairplot(data=df, vars=["Number of Bedrooms", "Number of Bathrooms", "Garden Size", "Square Footage", "Price", "Renovation Cost"], hue="Year Built")
g.fig.subplots_adjust(top=0.95)
plt.suptitle("House Features by Year in New York State", fontweight="bold", size=15)
plt.show()


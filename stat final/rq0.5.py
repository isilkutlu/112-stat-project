import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_excel("House_Price_temiz.xlsx")

df["Square_Footage"] = df["Square_Footage"]*10
# Create a new variable called Total_Rooms by adding Num_Bathrooms and Num_Bedrooms
df["Total_Rooms"] = df["Num_Bathrooms"] + df["Num_Bedrooms"]


# Bivariate and univariate density plot with Jointplot
sns.jointplot(x="Square_Footage", y="Total_Rooms", data=df, kind="kde")

#to show the visualization
plt.show()



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel()

# to obtain a certain data set from the data
locations = ['Albany', 'Buffalo', 'New York City', 'Rochester', 'Syracuse']
percentage_distribution = [25, 22.5, 12.5, 25, 15]

# to create pie-chart
plt.figure(figsize=(8, 8))
plt.pie(percentage_distribution, labels=locations, autopct='%1.1f%%', startangle=90, colors=plt.get_cmap('Accent_r').colors)
plt.title('Percentages of Houses on Sale by City in New York State')
plt.axis('equal')  # Set the circle as a smooth circle

# To show the visualization
plt.show()
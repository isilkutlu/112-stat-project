import pandas as pd
import numpy as np

df = pd.read_excel("House_Price.xlsx")

df = df.dropna(how='all')
print("Temizlenmiş DataFrame:")
print(df.head())
#The reset_index(drop=True) command is used to reset the index values in the data set and re-index them according to our wishes.df = df.reset_index(drop=True)
print("Yeniden İndekslenmiş DataFrame:")
#The head function is used to display the first 5 lines in the data set.print(df.head())

df.columns = df.iloc[0]
df = df[1:]
print("Başlıkları Ayarlanmış DataFrame:")
print(df.head())
#Examine the head and tail of the data frame
#tail command is used to print the last 5 lines in the data set.
#The #info() function provides documentation or information output that shows detailed information of an object (for example, a module, class, or function).
print(df.info())
print(df.head())
print(df.tail())
print("\nNaN Değer Kontrolü:")
print(df.isnull().sum())
# Reindexing
df = df.reset_index(drop=True)
# The columns command is used to create new headings instead of the indexes we reset.
df.columns = ["House_ID", "LOCATION", "HOUSE TYPE", "Num_Bedrooms","Num_Bathrooms","GARAGE TYPE","Garden_Size","Year_Built","MONTH BUILT","Square_Footage","Price","Renovation_Cost"]
print("Başlıkları Ayarlanmış DataFrame:")
print(df.head())

#Examine the variables and their data types.
print(df['House_ID'].apply(type).value_counts())
print(df['LOCATION'].apply(type).value_counts())
print(df['HOUSE TYPE'].apply(type).value_counts())
print(df['Num_Bedrooms'].apply(type).value_counts())
print(df['Num_Bathrooms'].apply(type).value_counts())
print(df['GARAGE TYPE'].apply(type).value_counts())
print(df['Garden_Size'].apply(type).value_counts())
print(df['Year_Built'].apply(type).value_counts())
print(df['MONTH BUILT'].apply(type).value_counts())
print(df['Square_Footage'].apply(type).value_counts())
print(df['Price'].apply(type).value_counts())
print(df['Renovation_Cost'].apply(type).value_counts())

#Performing the required operation for each column under that column

#House_ID
df['House_ID'] = pd.to_numeric(df['House_ID'], errors='coerce')
df = df.dropna(subset=['House_ID'])
df['House_ID'] = df['House_ID'].astype(str)

#LOCATION
print("LOCATION Sütunu:")
print(df['LOCATION'].head())
# Check NaN (null) values in 'location' column
print("\nLOCATION Sütunundaki NaN Değerler:")
print(df['LOCATION'].isnull().sum())

#HOUSE TYPE
print("\nHOUSE TYPE Sütunu Benzersiz Değerler:")
# To delete repeated data, the unique command is used to detect the presence of non-repetitive data in the data.
print(df['HOUSE TYPE'].unique())
df['HOUSE TYPE'] = df['HOUSE TYPE'].astype(str)
df['HOUSE TYPE'] = df['HOUSE TYPE'].str.lower().str.strip()
print("\nDüzeltildikten Sonraki HOUSE TYPE Sütunu Benzersiz Değerler:")
print(df['HOUSE TYPE'].unique())
df.dropna(subset=['HOUSE TYPE'], inplace=True)
df = df.reset_index(drop=True)
print("NaN Değerleri Silinmiş DataFrame:")
print(df.head())

#The data in the specified index was not persistently deleted. Since the category is data, I set it equal to the mode of the column.
df.at[23, "HOUSE TYPE"] = "single-family"


#num_bedrooms
print("Num_Bedrooms Sütunu Benzersiz Değerler:")
print(df['Num_Bedrooms'].unique())
# Converting the "Num Bedrooms" column to numeric format
# Converting categorical data to numeric
df['Num_Bedrooms'] =df['Num_Bedrooms'].replace(['one', 'three'], [1, 3])
df['Num_Bedrooms'] =pd.to_numeric(df['Num_Bedrooms'], errors='coerce')
df.dropna(subset=['Num_Bedrooms'], inplace=True)
print(df['Num_Bedrooms'].unique())
#The dropna command is used with the subset function to delete all missing values in a particular column.
#To make a function we apply to the #data set permanent, we use the inplace = True command.
#Num_Bathrooms
print("Num_Bathrooms Sütunu Benzersiz Değerler:")
print(df['Num_Bathrooms'].unique())
df['Num_Bathrooms'] = df['Num_Bathrooms'].replace(['two', 'three'], [2, 3])
df['Num_Bathrooms'] = pd.to_numeric(df['Num_Bathrooms'], errors='coerce')
df.dropna(subset=['Num_Bathrooms'], inplace=True)
int_values = df['Num_Bathrooms'][df['Num_Bathrooms'].apply(lambda x: isinstance(x, int))].unique()
df['Num_Bathrooms'] = df['Num_Bathrooms'].apply(lambda x: float(x) if x in int_values else x)

#GARAGE TYPE
print("GARAGE TYPE Sütunu Benzersiz Değerler:")
print(df['GARAGE TYPE'].unique())
#The strip function is used to delete extra spaces at the beginning and end of words.
#The capitalize command is used to capitalize the first letter of words.
df['GARAGE TYPE'] = df['GARAGE TYPE'].str.strip().str.capitalize()
df.dropna(subset=['GARAGE TYPE'], inplace=True)
print("GARAGE TYPE Sütunu Benzersiz Değerler:")
print(df['GARAGE TYPE'].unique())

#Garden Size
print("Garden_Size Sütunu Benzersiz Değerler:")
print(df['Garden_Size'].unique())
df['Garden_Size'] = df['Garden_Size'].str.replace('"', '').str.strip().str.capitalize()
df.dropna(subset=['Garden_Size'], inplace=True)
print("Garden_Size Sütunu Benzersiz Değerler:")
print(df['Garden_Size'].unique())

#Month built
#Converting data that actually belongs to date data type, even though it looks like numerical data, into date data type

df['MONTH BUILT'] = pd.to_datetime(df['MONTH BUILT'], errors='coerce', format='%m')
# Eğer tarih formatına çevrilemeyen değerler varsa, bu durumu temizle
df['MONTH BUILT'] = df['MONTH BUILT'].dt.month
df = df.dropna(subset=['MONTH BUILT'])

#Year Built
df['Year_Built'] = df['Year_Built'].apply(lambda x: int(str(x)[-4:]) if pd.notna(x) else x)
df['Year_Built'] = pd.to_datetime(df['Year_Built'], format='%Y', errors='coerce')
df['Year_Built'] = df['Year_Built'].apply(lambda x: x.year if pd.notna(x) else x)
unique_years = df['Year_Built'].unique()
print("Year_Built Sütunu Benzersiz Değerler:")
print(unique_years)

#Square_Footage
print("Square_Footage Sütunu Benzersiz Değerler:")
print(df['Square_Footage'].unique())
#Used to convert data in categorical form into numeric form.
df['Square_Footage'] = df['Square_Footage'].replace({2200: '2200', 1900: '1900', 2000: '2000', 1800: '1800'})
#errors = "coerce" command causes the data to become missing data in the form of NaN, instead of giving an error when an error occurs in numerical data.
df['Square_Footage'] = pd.to_numeric(df['Square_Footage'], errors='coerce')
df.dropna(subset=['Square_Footage'], inplace=True)
print("Square_Footage Sütunu Benzersiz Değerler:")
print(df['Square_Footage'].unique())

#Price
print("Price Sütunu Benzersiz Değerler:")
print(df['Price'].unique())
#lamda is used for small operations or short functions that will be used once.
#isinstance() function is used to check whether an object is of a certain type (data type).
#apply() function is used in the Pandas library to apply a specific operation on the data in the DataFrame.

integer_values = df['Price'][df['Price'].apply(lambda x: isinstance(x, int))].unique()
df['Price'] = df['Price'].apply(lambda x: int(x) if x in int_values else x)
print(df['Price'].apply(type).value_counts())

#Renovation cost
print("Renovation_Cost Sütunu Benzersiz Değerler:")
print(df['Renovation_Cost'].unique())
df['Renovation_Cost'] = pd.to_numeric(df['Renovation_Cost'], errors='coerce')
df.dropna(subset=['Renovation_Cost'], inplace=True)
print("Renovation_Cost Sütunu Eksik Değer Sayısı:", df['Renovation_Cost'].isnull().sum())

# DUPLICATE
print("Toplam Duplicatelerin Sayısı:", df.duplicated().sum())
columns_to_check_duplicates = ['LOCATION', 'HOUSE TYPE', 'Num_Bedrooms', 'Num_Bathrooms', 'GARAGE TYPE', 'Garden_Size', 'Year_Built', 'MONTH BUILT', 'Square_Footage', 'Price', 'Renovation_Cost']
duplicates = df.duplicated(subset=columns_to_check_duplicates, keep='first')
df.drop_duplicates(subset=columns_to_check_duplicates, keep='first', inplace=True)
df = df.reset_index(drop=True)
duplicate_count_after = df.duplicated().sum()
print(f" Son Duplicate Değer Sayısı : {duplicate_count_after}")

#12)Examine the variables and their data types again.
print(df['House_ID'].apply(type).value_counts())
print(df['LOCATION'].apply(type).value_counts())
print(df['HOUSE TYPE'].apply(type).value_counts())
print(df['Num_Bedrooms'].apply(type).value_counts())
print(df['Num_Bathrooms'].apply(type).value_counts())
print(df['GARAGE TYPE'].apply(type).value_counts())
print(df['Garden_Size'].apply(type).value_counts())
print(df['Year_Built'].apply(type).value_counts())
print(df['MONTH BUILT'].apply(type).value_counts())
print(df['Square_Footage'].apply(type).value_counts())
print(df['Price'].apply(type).value_counts())
print(df['Renovation_Cost'].apply(type).value_counts())

#Descriptive Statistics
#describe() function is used in the Pandas library to get the basic statistical summary of a DataFrame.
#This function provides central tendency, dispersion, and other statistical properties of numerical data within the DataFrame.
numeric_stats = df.describe()
print(numeric_stats)
#Determining limits by taking the standard deviation of the num_bedrooms column
std_dev = df['Num_Bedrooms'].std()
upper_limit = df['Num_Bedrooms'].mean() + 3 * std_dev
lower_limit = df['Num_Bedrooms'].mean() - 3 * std_dev
unusual_Num_Bedrooms = df[(df['Num_Bedrooms'] < lower_limit) | (df['Num_Bedrooms'] > upper_limit)]
print(unusual_Num_Bedrooms)

#Determining limits by taking the standard deviation of the num_Bathrooms column
std_dev = df['Num_Bathrooms'].std()
upper_limit = df['Num_Bathrooms'].mean() + 3 * std_dev
lower_limit = df['Num_Bathrooms'].mean() - 3 * std_dev
unusual_Num_Bathrooms = df[(df['Num_Bathrooms'] < lower_limit) | (df['Num_Bathrooms'] > upper_limit)]
print(unusual_Num_Bathrooms)

#Determining limits by taking the standard deviation of the Price column
std_dev = df['Price'].std()
upper_limit = df['Price'].mean() + 3 * std_dev
lower_limit = df['Price'].mean() - 3 * std_dev
unusual_Price = df[(df['Price'] < lower_limit) | (df['Price'] > upper_limit)]
print(unusual_Price)

#Determining limits by taking the standard deviation of the Renovation_Cost column
std_dev = df['Renovation_Cost'].std()
upper_limit = df['Renovation_Cost'].mean() + 3 * std_dev
lower_limit = df['Renovation_Cost'].mean() - 3 * std_dev
unusual_Renovation_Cost = df[(df['Renovation_Cost'] < lower_limit) | (df['Renovation_Cost'] > upper_limit)]
print(unusual_Renovation_Cost)

#Determining limits by taking the standard deviation of the Square_Footage column
std_dev = df['Square_Footage'].std()
upper_limit = df['Square_Footage'].mean() + 3 * std_dev
lower_limit = df['Square_Footage'].mean() - 3 * std_dev
unusual_square_footage = df[(df['Square_Footage'] < lower_limit) | (df['Square_Footage'] > upper_limit)]
print(unusual_square_footage)

#Determine outliers
# Assuming 'df' is your DataFrame
# Step 1: Define the numerical columns
numerical_columns = ['Renovation_Cost', 'Square_Footage', 'Price', 'Num_Bathrooms', 'Num_Bedrooms']
# Step 2: Define a function to replace outliers with the mean

def replace_outliers_with_mean(column):
    # Calculate the mean and standard deviation
    mean_val = df[column].mean()
    std_val = df[column].std()
    # According to Chebyshew's Theorem, when you go to the lower and upper 3 standard deviations of a numerical data, there is a 99.7% probability that you will keep it in the outline.
    # We set a threshold value to define Outlier.
    threshold = 3
    # Filling in missing values in numerical columns with the average values of those columns
    df[column] = np.where(np.abs((df[column] - mean_val) / std_val) > threshold, mean_val, df[column])
# Step 3: We use a for loop to apply the filling process with the average value to each column.
for column in numerical_columns:
    replace_outliers_with_mean(column)

#We check whether the length data in the data set are used in the same unit. They must all be the same unit.
def check_units_consistency(Square_Footage, m, cm):
    # Take a specific column and its units to check if the units are consistent
    consistent_units = all(df[Square_Footage].apply(lambda x: str(x).endswith(m) or str(x).endswith(cm)))
    return consistent_units
consistent_square_footage_units = check_units_consistency('Square_Footage', 'm', 'cm')
print("Consistent Square Footage Units:", consistent_square_footage_units)
unique_square_footage_units = df['Square_Footage'].apply(lambda x: str(x)[-2:]).unique()
print("Unique Square Footage Units:", unique_square_footage_units)

def convert_units_to_meters(value, unit):
    if unit == 'cm':
        return value / 100.0
    else:
        return value
# Converting the units in the "Square Footage" column to the same format
df['Square_Footage'] = df.apply(lambda row: convert_units_to_meters(row['Square_Footage'], 'cm'), axis=1)

#To find out the percentage of missing data in columns

missing_values = df.isnull().sum()
missing_percentages = (missing_values / len(df)) * 100
missing_info = pd.DataFrame({'Missing_Values': missing_values, 'Percentage': missing_percentages})
low_threshold = 60
high_threshold = 60

if 'Square_Footage' in missing_info.index:
    if missing_info.loc['Square_Footage', 'Percentage'] < low_threshold:
        df['Square_Footage'].fillna(df['Square_Footage'].mean(), inplace=True)
    else:
        df.drop(columns=['Square_Footage'], inplace=True)

# Step 4: Filling the missing values with the average value for columns with a missing data rate lower than the lower limit we set in a column with numerical data.
# If it has more missing data than the lower threshold we set, delete that column directly
for col in ['Renovation_Cost', 'Price', 'Num_Bedrooms', 'Num_Bathrooms']:
    if col in missing_info.index:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if missing_info.loc[col, 'Percentage'] < low_threshold:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df.drop(columns=[col], inplace=True)

#Transferring the clean data we obtained to a clean Excel file
df.to_excel('House_Price_temiz.xlsx', index=False)
print("New Excel file is included: House_Price_temiz.xlsx")



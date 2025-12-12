# # Malik Sherdil
# # WEEK 2 TASKS
# # PANDAS

# import pandas as pd

# # Load CSV file
# data = pd.read_csv('data.csv')

# # Load EXCEL file
# df = pd.read_excel('data.xlsx')

# # Save CSV
# data.to_csv('output.csv', index=False)

# # Save EXCEL
# df.to_excel('output.xlsx', index=False)

# # Data inspectio and underanding
# df.head()        # First 5 rows
# df.tail()       # Last 5 rows
# df.info()       
# df.describe()  
# df.shape      
# df.columns      

# # indexing and Slicing
# subset = df[['Column1', 'Column2']]
# row = df.iloc[0]


# # cleaning and preprocessing
# df.dropna(inplace=True)
# df.fillna(0, inplace=True)
# df['Column1'] = df['Column1'].astype(float)

# # Removing Duplicates
# df.drop_duplicates(inplace=True)

# # change data types
# df['Column2'] = pd.to_datetime(df['Column2'])

# # sorting
# df.sort_values(by='Column1', ascending=True, inplace=True)

# # Group by and aggregation
# grouped = df.groupby('Category').agg({'Column1': 'sum', 'Column2': 'mean'})

# # vectorized operations
# df['NewColumn'] = df['Column1'] * 2 + df['Column2']

# # apply map , transform
# # map
# df['Gender'] = df['Gender'].map({'Male': 'M', 'Female': 'F'})

# # apply
# df['Age category'] = df['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Minor')

# # transform
# df["Age_Norm"] = df["Age"].transform(lambda x: (x - x.mean()) / x.std())

# # Missing Data Handling
# df.isnull().sum()

# # Fill missing values
# df["Age"]= df["Age"].fillna(df["Age"].mean())

# # Exporting cleaned data
# df.to_csv('cleaned_data.csv', index=False)
# df.to_excel('cleaned_data.xlsx', index=False)

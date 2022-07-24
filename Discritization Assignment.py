# Discritization 



import pandas as pd
data = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\iris.csv")
data.head()
data.describe()

# Discritization for sepal_length

data['Sepal_Length_new'] = pd.cut(data['Sepal_Length'], bins=[min(data.Sepal_Length) - 1, 
                                                  data.Sepal_Length.mean(), max(data.Sepal_Length)], labels=["Low","High"])
data.head()
data.Sepal_Length_new.value_counts()

 ## Discritization for Sepal_width

data['Sepal_Width_new'] = pd.cut(data['Sepal_Width'], bins=[min(data.Sepal_Width) - 1, 
                                                  data.Sepal_Width.mean(), max(data.Sepal_Width)], labels=["Low","High"])
data.head()
data.Sepal_Width_new.value_counts()

# Discritization for Petal_Length

data['Petal_Length_new'] = pd.cut(data['Petal_Length'], bins=[min(data.Petal_Length) - 1, 
                                                  data.Petal_Length.mean(), max(data.Petal_Length)], labels=["Low","High"])
data.head()
data.Petal_Length_new.value_counts()


 ## Discritization for Petal_Width

data['Petal_Width_new'] = pd.cut(data['Petal_Width'], bins=[min(data.Petal_Width) - 1, 
                                                  data.Petal_Width.mean(), max(data.Petal_Width)], labels=["Low","High"])
data.head()
data.Petal_Width_new.value_counts()


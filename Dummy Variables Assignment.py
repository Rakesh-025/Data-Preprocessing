##################################################
################## Dummy Variables ###############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# we use Animal_category dataset
df = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\animal_category.csv")

df.columns # column names
df.shape # will give u shape of the dataframe

# drop emp_name column
df.drop(['Index'], axis=1, inplace=True)
df.dtypes

# Create dummy variables
df_new = pd.get_dummies(df)
df_new_1 = pd.get_dummies(df, drop_first = True)
# we have created dummies for all categorical columns

##### One Hot Encoding works
df.columns
df = df[['Animals','Gender','Homly','Types']]


from sklearn.preprocessing import OneHotEncoder
# Creating instance of One Hot Encoder
enc = OneHotEncoder() # initializing method

enc_df = pd.DataFrame(enc.fit_transform(df.iloc[:,0:]).toarray())


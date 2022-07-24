\####### Standardization #########
import pandas as pd
import numpy as np


from sklearn.preprocessing import StandardScaler
d = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\Seeds_data.csv")

a = d.describe()
# Initialise the Scaler
scaler = StandardScaler()
# To scale data
df = scaler.fit_transform(d)
# Convert the array back to a dataframe
dataset = pd.DataFrame(df)
res = dataset.describe()

import pandas as pd

df = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes/onlineretail.csv")

#type casting
# Now we will convert 'float64' into 'int64' type. 
df.UnitPrice = df.UnitPrice.astype('int64') 
df.dtypes


#Identify duplicates records in the data
duplicate = df.duplicated()
sum(duplicate)

#Removing Duplicates
data = df.drop_duplicates() 


#Exploratory Data Analysis
#Measures of Central Tendency / First moment business decision
data.Description.mode()


from sklearn.impute import SimpleImputer
import numpy as np
# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
data["Description"] = pd.DataFrame(mode_imputer.fit_transform(data[["Description"]]))
data.Description.isnull().sum()  # all descriptive records replaced by mode
data.isnull().sum()

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np

plt.hist(data.UnitPrice) #histogram

plt.boxplot(data.UnitPrice) #boxplot

import seaborn as sns

sns.scatterplot(data=df, x="UnitPrice", y="Description")








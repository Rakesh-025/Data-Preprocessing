

#################### Missing Values Imputation ################################
import numpy as np
import pandas as pd

# load the dataset
# use modified ethnic dataset
df = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes/claimants.csv") # for doing modifications

# check for count of NA'sin each column
df.isna().sum()

# Create an imputer object that fills 'Nan' values
# Mean and Median imputer are used for numeric data (CLMAGE)
# Mode is used for discrete data (ex: CLMSEX, CLMINSUR, SEATBELT)

# for Mean, Meadian, Mode imputation we can use Simple Imputer or df.fillna()
from sklearn.impute import SimpleImputer

# Mean Imputer 
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df["CLMAGE"] = pd.DataFrame(mean_imputer.fit_transform(df[["CLMAGE"]]))
df["CLMAGE"].isna().sum()
df.isna().sum()

# Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMAGE"]]))
df["CLMAGE"].isna().sum()  # all 2 records replaced by median 
df.isna().sum()

# Mode Imputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df["CLMSEX"] = pd.DataFrame(mode_imputer.fit_transform(df[["CLMSEX"]]))
df["CLMINSUR"] = pd.DataFrame(mode_imputer.fit_transform(df[["CLMINSUR"]]))
df["SEATBELT"] = pd.DataFrame(mode_imputer.fit_transform(df[["SEATBELT"]]))
df.isnull().sum()  # all CLMINSUR,CLMINSUR, SEATBELT records replaced by mode

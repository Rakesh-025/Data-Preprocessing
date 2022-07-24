
################ Transformation #####################


# Normal Quantile-Quantile Plot ####
import pandas as pd
import scipy.stats as stats
import pylab
import matplotlib.pyplot as plt
df=pd.read_csv (r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes/calories_consumed.csv")
# Checking Whether data is normally distributed
df.columns
stats.probplot(df["Weight gained (grams)"], dist="norm", plot=pylab)

stats.probplot(df["Calories Consumed"], dist="norm", plot=pylab)
#transformation to make Weight gained (grams), Calories Consumed variables normal
import numpy as np
stats.probplot(np.log(df["Weight gained (grams)"]),dist="norm",plot=pylab)
stats.probplot(np.log(df["Calories Consumed"]),dist="norm",plot=pylab)




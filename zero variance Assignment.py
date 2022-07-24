import pandas as pd
from sklearn.feature_selection import VarianceThreshold

data = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\Z_dataset.csv")
#drop id and colour
data.info()
data.drop(['Id','colour'], axis=1, inplace=True)


var_thres=VarianceThreshold(threshold=0)
var_thres.fit(data)                            
var_thres.get_support()


data["square.length"].var()

data["square.breadth"].var()
data["rec.Length"].var()
data["rec.breadth"].var()

#variance value of squarebreadth is nearly equal to zero(0.189) so we have to drop the column
data.drop(['square.breadth'], axis=1,inplace=True)

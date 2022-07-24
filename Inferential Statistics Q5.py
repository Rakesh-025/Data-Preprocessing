import pandas as pd

# to read the file
df=pd.read_excel(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\data preprocesssing\Assignment_module02 (1).xlsx")
         
df.info()

#       ( for points )
#    measures of central tendency  

df.Points.mean()
df.Points.median()
df.Points.mode()
# Measures of Dispersion / Second moment business decision
df.Points.var() # variance
df.Points.std() # standard deviation
range = max(df.Points) - min(df.Points) # range
range

#    for score
#   measures of central tendency 
df.Score.mean()
df.Score.median()
df.Score.mode()
# Measures of Dispersion / Second moment business decision
df.Score.var() # variance
df.Score.std() # standard deviation
range = max(df.Score) - min(df.Score) # range
range

 #    for weigh
#    measures of central tendency
df.Weigh.mean()
df.Weigh.median()
df.Weigh.mode()
# Measures of Dispersion / Second moment business decision
df.Weigh.var() # variance
df.Weigh.std() # standard deviation
range = max(df.Weigh) - min(df.Weigh) # range
range




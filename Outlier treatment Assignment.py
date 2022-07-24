############## Outlier Treatment ###############
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes/boston_data.csv")
df.dtypes

# finding outliers in crim
sns.boxplot(df.crim)


# Detecting of outliers (find limits for crim based on IQR)
IQR = df['crim'].quantile(0.75) - df['crim'].quantile(0.25)
lower_limit = df['crim'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['crim'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for crim ###############
# pip install feature_engine   # install the package
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['crim'])

df_t = winsor.fit_transform(df[['crim']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.crim)


###################################################
#finding outliers in zn
sns.boxplot(df.zn)

# Detection of outliers (find limits for zn based on IQR)
IQR = df['zn'].quantile(0.75) - df['zn'].quantile(0.25)
lower_limit = df['zn'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['zn'].quantile(0.75) + (IQR * 1.5)

### winsorization for zn ####
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['zn'])

df_t = winsor.fit_transform(df[['zn']])



# lets see boxplot
sns.boxplot(df_t.zn)

############################################################
# finding outliers in indus
sns.boxplot(df.indus)
# no outliers in indus column

############################################################
# finding outliers in chas
sns.boxplot(df.chas)

# Detection of outliers (find limits for chas based on IQR)
IQR = df['chas'].quantile(0.75) - df['chas'].quantile(0.25)
lower_limit = df['chas'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['chas'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for chas ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['chas'])

df_t = winsor.fit_transform(df[['chas']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.chas)


##########################################################
# let's find outliers in nox
sns.boxplot(df.nox)
# no outliers in nox column


##########################################################
#  finding outliers in rm
sns.boxplot(df.rm)

# Detection of outliers (find limits for rm based on IQR)
IQR = df['rm'].quantile(0.75) - df['rm'].quantile(0.25)
lower_limit = df['rm'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['rm'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for rm ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['rm'])

df_t = winsor.fit_transform(df[['rm']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.rm)


############################################################
#  finding outliers in age
sns.boxplot(df.age)
# no outliers in age column


############################################################
#  finding outliers in dis
sns.boxplot(df.dis)

# Detection of outliers (finding limits for dis based on IQR)
IQR = df['dis'].quantile(0.75) - df['dis'].quantile(0.25)
lower_limit = df['dis'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['dis'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for dis  ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['dis'])

df_t = winsor.fit_transform(df[['dis']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.dis)

###########################################################
#  finding outliers in rad
sns.boxplot(df.rad)
# no outliers in rad column


###########################################################
# finding outliers in tax
sns.boxplot(df.tax)
# no outliers in tax column


###########################################################
#  finding outliers in ptratio
sns.boxplot(df.ptratio)

# Detection of outliers (find limits for ptratio based on IQR)
IQR = df['ptratio'].quantile(0.75) - df['ptratio'].quantile(0.25)
lower_limit = df['ptratio'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['ptratio'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for ptratio  ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['ptratio'])

df_t = winsor.fit_transform(df[['ptratio']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.ptratio)


############################################################
#  finding outliers in black
sns.boxplot(df.black)

# Detection of outliers (find limits for black based on IQR)
IQR = df['black'].quantile(0.75) - df['black'].quantile(0.25)
lower_limit = df['black'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['black'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for black ###############
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['black'])

df_t = winsor.fit_transform(df[['black']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.black)


############################################################
#  finding outliers in lstat
sns.boxplot(df.lstat)

# Detection of outliers (find limits for lstat based on IQR)
IQR = df['lstat'].quantile(0.75) - df['lstat'].quantile(0.25)
lower_limit = df['lstat'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['lstat'].quantile(0.75) + (IQR * 1.5)

############### Winsorization for lstat ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['lstat'])

df_t = winsor.fit_transform(df[['lstat']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.lstat)


############################################################
#  finding outliers in medv
sns.boxplot(df.medv)

# Detection of outliers (find limits for medv based on IQR)
IQR = df['medv'].quantile(0.75) - df['medv'].quantile(0.25)
lower_limit = df['medv'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['medv'].quantile(0.75) + (IQR * 1.5)


############### Winsorization for medv  ###############

from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['medv'])

df_t = winsor.fit_transform(df[['medv']])

# we can inspect the minimum caps and maximum caps 
# winsor.left_tail_caps_, winsor.right_tail_caps_

# lets see boxplot
sns.boxplot(df_t.medv)

###########################################################

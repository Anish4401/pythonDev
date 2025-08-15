import seaborn as sns
df=sns.load_dataset('titanic')
print(df.head(10))

print(df.isnull().sum())
#here we are just expleorng the the missign values in diff condtion while filling the datasets  here we found the multiple missing  values where we will 
#try to impute them and with the impuetation Missing  technique
# 1- Mean value Imputation
plot=sns.barplot(df['age'])
print(plot)
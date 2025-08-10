#Pandas:
#Pandas is a powerful data analysis and manipulation library for Python.
#DataFrame And Series :
#DataFrame: 2D data structure, like a table with rows and columns.
#Series: 1D data structure, like a single column of a DataFrame like array ,objects of the same type.
import pandas as pd
# data=[1,2,3,5,6]
# #Creating a series
# series=pd.Series(data)  #it will create a series from the data
# print(series)
# #now creating sereis with dictionary :
# data={'a':1,'b':2,"c":3,'d':4,'e':5}
# print(pd.Series(data))   #Now here its acting as keys & value and show the values based on the keys
# #index
# index=['a','b','c','d','e']
# print(pd.Series(data,index=index))


#DataFrame : 
# now defining it with dictionary and in list :
data={
    'Name':['Anish','Manish','Sayan'],
    'Age':[24,28,11],
    'places':['asansol','kolkata','hariPara']
}
df = pd.DataFrame(data) # will give the values of all the keys in list
print(df)
print(type(df))
print(df['Name']) #will give the list of all the names 
print(df.loc[1])# it will access the location of that perticular column .
print(df.iloc[0][0]) #it will give the value of that perticular index/location
print(df.at[1,"places"])# it will give the specific value on the index 
print(df.iat[1,1])# it will the specific values at the location taking rows & cols
df['business']=["Travel","Trade","IT"] #It will create the new column with these values for that key
print(df)# will print the latest list
#Remove the cols:
df.drop('business',axis=1,inplace=True) # now it will paramently removed it 
print(df)

#now some operation to increse the age based on year 
df['Year']=[2024,2024,2024]
df["Age"]=df['Age']+1 # now this will increse the age of the age cols values
print(df)
#now if i want to drop something then 
df.drop(0,inplace=True) # it will drop all the values of that perticular  rows
print(df)
print("Statical format resposne:\n",df.describe()) # it generally give the stats of the data

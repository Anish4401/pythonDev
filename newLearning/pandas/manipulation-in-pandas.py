
# import pandas as pd
# df=pd.read_csv('data.csv')
# print(df.head(5)) # it will read the file and give the first 5 datas
# print(df.tail(7)) # it will give the last 7 datas
# print(df.dtypes)
# #Handing missing values:
# print(df.isnull().any()) # it will check if their is missing val if then give it as true if not then false
# print(df.isnull().sum()) # it will give the missing values 
# print(df.fillna('0'))
# print(df.at[65,"Description"]) #it will give the name of that index

# #renaming the cols name 
# print(df.rename(columns={"Description":"Transaction Name"})) # now this will repalce the name with country Name
# #now changing the datatypes
# # df['Symbol_New']=df[''].astype('string') #it will set as the string as dataType as it will create a copy
# # print(df.dtypes['Symbol_New'])
# print(df.describe())
# df['Deposits']=df['Deposits'].replace('[^0-9.]','',regex=True) #here we need to remove the element except all 0-9 than this and then convert string to numberic
# df['Deposits']=pd.to_numeric(df['Deposits'],errors='coerce')
# print(df['Deposits'].mean())
# # print(df.groupby(['Balance'])["Withdrawls"].mean())
# df['Withdrawls']=df['Withdrawls'].replace('[^0-9.]','',regex=True)
# df['Converted_Withdrawls']=pd.to_numeric(df['Withdrawls'])
# print(df.groupby('Balance')["Converted_Withdrawls"].mean())
# print(df.groupby(['Deposits','Balance'])['Withdrawls'].sum())  #here we gruping based on two category
# #Will apply the all aggregate func
# groupdata_agg=df.groupby('Description')['Converted_Withdrawls'].agg(["sum","mean","count","median"])
# print(groupdata_agg)
# # now we will work on merging & joining DataFrames
# data=pd.DataFrame({
#     "Name":["Anish","Manish","Golu"],
#     "Age":[24,28,12]

# })
# data1=pd.DataFrame({
#     "Name":["Anish","Manish"],
#     "Salary":[15000,76000]
# })
# print(data)
# data2=pd.merge(data,data1, on="Name",how="inner")  #now here we are merging the two datasets based on the Name and inner join is performed
# print(data2)

#Now reading the json file.
from io import StringIO
data = '''
{
    "name": "rrr",
    "description": "hii i am travel",
    "type": 1,
    "count_leave": "10",
    "status": 1
    
}
'''
import pandas as pd
data=pd.read_json(StringIO(data),typ="series")
print(data)
print(data.to_json(orient="records")) #this will give the keys values

#Reading the Urls 
# import bs4 from BeautifulSoup
url="https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df=pd.read_html(url)
print(df)
data=pd.read_excel("vehicleTableExcel.xlsx")
print(data.head(3))



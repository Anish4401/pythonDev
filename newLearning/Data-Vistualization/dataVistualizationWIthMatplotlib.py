import matplotlib.pyplot as plots
# x=[1,2,3,4,5]
# y=[1,4,9,16,60]
# print(plots.plot(x,y))  # it will create a daigram to create with x-axis & y-axis showing the coordinates
# print(plots.xlabel("X-axis"))
# print(plots.title("Table view"))

# print(plots.plot(x,y,linestyle='--',marker='o',linewidth=3))#here we are just enchanign the view of the line in the daigram
# print(plots.show())\

#Multiple plot 
# x=[1,2,3,4,5,6]
# y=[1,2,3,4,5,6]
# y1=[8,10,1,14,20,28]
# plots.figure(figsize=(7,5))
# plots.subplot(1,2,1)
# plots.plot(x,y,color="red")
# plots.title("Plot 1")
# plots.subplot(2,2,2)
# plots.plot(x,y1,color="green" ,marker="o")
# plots.title("Plot 2")

#bar plot chart view 
# category=['A','B','C']
# val=[6,7,2]
# plots.bar(category,val,color="gray",linewidth=3)

# print(plots.show())

#histogram
# data=[1,2,3,3,3,4,4,4,4,5,5,5,5,5]
# plots.hist(data,bins=5,color='orange',edgecolor='black')
# print(plots.show())
#pie chart
# data=[10,20,30,40]
# labels=['A','B','C','D']
# colors=['red','blue','green','yellow']
# explode=[0.1,0,0,0]
#   # this will just explode the first part of the pie chart
# (plots.pie(data,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,explode=explode))
# print(plots.show())

# lets test with the some datas
import pandas as pd
the_csv=pd.read_csv("currency.csv")
read_the_csv=the_csv.head(10)  # it will read the first 10 rows of the csv file
print(read_the_csv)
# lets plot the data with the csv file
read_the_csv.info()
  # it will give the info of the csv file
  # lets plot pie chart with the csv file
data=read_the_csv['Code']  # it will take the value of the Value column
labels=read_the_csv[['Code','Symbol',"Name"]]
colors=['red','blue','green','yellow']
explode=[0.1,0,0,0]
plots.pie(data,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,explode=explode)
print(plots.show())


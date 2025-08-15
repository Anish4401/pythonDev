import seaborn as sns
#Basic plot with seaborn
trips=sns.load_dataset('tips')
print(trips.head(10))  # it will read the first 10 rows of the csv file
#now will show in the chart
import matplotlib.pyplot as plt
# sns.scatterplot(data=trips,x="total_bill",y="tip",hue="day",style="time")
# plt.title("Total Bill vs Tip")
# plt.xlabel("Total Bill")
# plt.ylabel("Tip")
# # plt.show()  # it will show the chart with the total bill vs tip
# #Now will show the line chart with the total bill vs tip
# sns.lineplot(data=trips,x="total_bill",y="tip",hue="day",style="time")
# plt.title("Total Bill vs Tip")
# # plt.show()  # it will show the chart with the total bill vs tip

# sns.violinplot(data=trips,x="day",y="total_bill",hue="time",split=True)
# plt.title("Total Bill vs Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# # plt.show()  # it will show the chart with the total bill vs day

# sns.histplot(data=trips,x="total_bill",)
# plt.title("Total Bill Histogram")
# plt.xlabel("Total Bill")
# plt.ylabel("Count")
# # plt.show()  # it will show the histogram of the total bill
# #pair plot is basically used to show the all the plots into one chart
# sns.pairplot(data=trips)
# # plt.show()

# #coorilation of the daata and seaborn
# corr=trips[["total_bill",'tip','size']].corr()
# print(corr)
# # sns.heatmap(corr,annot=True,cmap="coolwarm")

#Now we will custamise with some dataset with matplotlib and seaborn 
import pandas as pd
curr=pd.read_csv("currency.csv")
print(curr.head(10))
# plt.rcParams['font.family'] = 'Noto Sans Bengali'  # Set the font family to Noto Sans Bengali
sns.histplot(data=curr,x="Code",y="Symbol",palette="viridis")
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.title("Currency Val")
plt.xlabel("Code") 
plt.ylabel("Symbol")
plt.show()
# from sklearn.linear_model import LinearRegression
# import pandas as pd

# Sample data
# data = {'hours_studied': [1, 2, 3, 4, 5],
#         'marks_obtained': [20, 40, 60, 80, 100]}
landRate={'year':[2010,2013,2017,2020],
          'rate':[5,7,9,11]}

df = pd.DataFrame(landRate)

X = df[['year']]  # Features
y = df['rate']   # Target

model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours of study
print(model.predict([[2025]])) # i think linear regression is not working properly here for the year 2025 so we will use another method to predict the rate for 2025


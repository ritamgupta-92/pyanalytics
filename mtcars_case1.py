#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data
#structure

#summary

#print first / last few rows
import pandas as pd
type(mtcars)
print(mtcars.head())
print(mtcars.tail())
#print number of rows
print(mtcars.shape[0])

#number of columns
print(mtcars.shape[1])

#print names of columns
print(mtcars.columns.tolist())
#Filter Rows
#cars with cyl=8
print(mtcars.loc[mtcars['cyl']==8])

#cars with mpg <= 27
print(mtcars.loc[mtcars['cyl']==8])
#rows match auto tx
#print(mtcars.loc[mtcars['cyl']==8])
#First Row
print(mtcars.head(1))

#last Row
print(mtcars.tail(1))

# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(mtcars.iloc[[1,4,7,25],[1,6,7]])

# first 5 rows and 5th, 6th, 7th columns of data frame
print(mtcars.iloc[1:5,[5,6,7]])
#rows between 25 and 3rd last
print(mtcars.iloc[25:-3,:])
#alternative rows and alternative column
print(mtcars.iloc[::2,::2])
#find row with Mazda RX4 Wag and columns cyl, am
print(mtcars.loc['Mazda RX4 Wag',['cyl','am']])
#find row betwee Merc 280 and Volvo 142E and columns cyl, am
print(mtcars.loc['Merc 280':'Volvo 142E',['cyl','am']])

# mpg > 23 or wt < 2
print(mtcars.loc[(mtcars['mpg'] > 23) | (mtcars['wt'] < 2)])

#using lambda for above


#with or condition

#find unique rows of cyl, am, gear
#mtcars.loc[mtcars[['cyl','am','gear']].duplicated(keep=False), :]

#create new columns: first make a copy of mtcars to mtcars2
mtcars2 = mtcars
#keeps other cols and divide displacement by 61
mtcars2['disp_1'] = mtcars2['disp']/61
# multiple mpg * 1.5 and save as original column
mtcars2['mpg'] = mtcars2['mpg']*1.5
print(mtcars2.head())


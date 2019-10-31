import pandas as pd
import numpy as np

spam_dataset = pd.read_csv('spambase.data')

#get the number of rows and cols
print(spam_dataset.shape)

#get the column names 0
print(spam_dataset['0'])

#get the min value within column named 0
print(spam_dataset['0'].min())

#get mean max min percentailes std statistics of the dataframe
print(spam_dataset.describe())

#see the type of this column
print(type(spam_dataset['0']))

#panda version of filter
print(spam_dataset[spam_dataset['0']>0.5])

#to see the index information of the dataframe
print(spam_dataset.index)

#set a columns as index to replace the default index, inplace=True means to modify the current dataframe instead of creating a new one
#you can also set columns that contain duplicate values to be index

spam_dataset.set_index('0',inplace=True)

print(spam_dataset)
print(spam_dataset.loc[0.88])

#reset dataframe's index to default index
spam_dataset.reset_index(inplace=True)
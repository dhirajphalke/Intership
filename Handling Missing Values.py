#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv(r"C:\Users\dhira\OneDrive\Desktop\NFL Play by Play 2009-2017 (v4).csv")
data


# In[4]:


# set seed  for reproducibility
np.random.seed(0)


# In[5]:


data.head()


# Looks like there are some missing values in data set

# In[6]:


# To check how many missing values we have in data set


# In[11]:


missing_values_count = data.isnull().sum()
missing_values_count[0:20]


# Its seems like a lot it might be helpful too see whaat percentage of the vlaues in our data were missing to give us a better sense of the scale of this problem.

# In[14]:


# how many total missing values do we have 
total_cells = np.product(data.shape)
total_missing = missing_values_count.sum()
#percentage  of missing value
percentage_missing = (total_missing/total_cells)*100
print(percentage_missing)


# Oh, almost 25% of the cells in this dataset are empty.
# 

# In[15]:


#drop missing values


# In[16]:


# remove all rows that contain a missing values
data.dropna()


# Looks like that removed all our data . This is because every row in our dataset had a atleast
# one missing values

# In[18]:


# remove all columns that contains  a missing value
column_with_na_dropped = data.dropna(axis=1)
column_with_na_dropped.head()


# In[21]:


#just check how much data we lose?
print("Columns in original dataset:", data.shape[1])
print("Columns with na dropped:", column_with_na_dropped.shape[1])


# In[ ]:


#Filling in missing values automatically


# In[25]:


# get small subset of our data set
subset_data = data.loc[:, 'EPA':'Season'].head()
subset_data


# In[26]:


#replace all NA's with 0
subset_data.fillna(0)


# In[27]:


# replace all NA's the value that comes directly after in the same column,
# then replace  all the remaining na's with 0
subset_data.fillna(method='bfill', axis=0).fillna(0)


# In[ ]:





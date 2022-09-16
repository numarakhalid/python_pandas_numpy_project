#!/usr/bin/env python
# coding: utf-8

# # weather dataset

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv(r"C:\Users\mujjj\Downloads\1. Weather Data.csv")


# In[3]:


data.head()


# In[4]:


#seeing shape od data
data.shape


# In[5]:


#seeing index number in data
data.index


# In[6]:


data.columns


# In[7]:


#for checking the datatype of data
data.dtypes


# In[8]:


#finding unique value in weather column
data['Weather'].unique()


# In[9]:


data.nunique()


# In[10]:


#for not null value in dataset
data.count()


# In[11]:


#it show the the unique value with their count
data['Weather'].value_counts()


# In[12]:


data.info()


# # find the unique "wind speed" values in data 

# In[13]:


data.columns


# In[14]:



data.nunique()


# In[15]:


data['Wind Speed_km/h'].nunique()


# In[16]:


data['Wind Speed_km/h'].unique()


# # find the number of times when weather is exaclty clear

# In[17]:


data.columns


# In[18]:


data.Weather.value_counts()


# In[25]:


data.head(2)
data[data.Weather=='Clear']


# In[ ]:





# # Find the number of time when the wind is exactly 4km/h

# In[29]:


data.columns


# In[34]:


data[data['Wind Speed_km/h']==4]


# # find all null values in data

# In[36]:


data.isnull().sum()


# In[37]:


data.notnull().sum()


# # Rename the column name 'weather' to 'weather condition'

# In[6]:


data.rename(columns={'Weather' : 'Weather condition'},inplace=True)


# In[7]:


data.head()


# # what is the mean and standard deviation of visibility

# In[8]:


data.columns


# In[9]:


data.Visibility_km.mean()


# In[10]:


data.Visibility_km.std()


# # what is the variance of 'Relative Humidity' in this data

# In[11]:


data.columns


# In[12]:


data['Rel Hum_%'].var()


# # Find the instances when 'snow' was recorded

# In[13]:


data.head(2)


# In[15]:


data['Weather condition'].value_counts()


# In[17]:


data[data['Weather condition']=='Snow']


# In[21]:


data[data['Weather condition'].str.contains('Snow')].tail(10)


# # Find all instances when 'Wind speed is above 24' and 'visibilty is 25'

# In[22]:


data.columns


# In[28]:


data[(data[ 'Wind Speed_km/h']>24) & (data['Visibility_km']==25)].head(10)


# # what is the mean of each column against each 'Weather condition'

# In[31]:


data.groupby('Weather condition').mean().head(5)


# # what is min and max value of each columns against each 'weather condition'

# In[35]:


data.groupby('Weather condition').max().head(5)


# In[36]:


data.groupby('Weather condition').min().head(5)


# # show all records  where weather condition is fog

# In[40]:


data[data['Weather condition']=='Fog'].head(5)


# # Find all instance when 'weather is clear' or visbilty is above to 40

# In[42]:


data.columns


# In[44]:


data[(data['Weather condition']=='Clear') | (data['Visibility_km']>40)]


# # Find all instance when
# A.  'Weather is clear' and 'Relative Humisity is greater then 50
# or
# B. 'Visibilty is above to 40

# In[45]:


data.columns


# In[48]:


data[(data['Weather condition']=='Clear') & (data['Rel Hum_%']>50) | data['Visibility_km']>40)]


# In[ ]:





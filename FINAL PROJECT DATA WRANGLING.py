#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import numpy as np
import os
import warnings
import seaborn as sns
import matplotlib.pyplot as plt


# In[75]:


df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')


# In[76]:


df


# # High Level Data Understanding:

# a)Find no. of rows & columns in the dataset
# 

# In[77]:


print(f" Number of columns in dataset is :-  {len(df.columns)}")


# In[78]:


print(f" Number of rows in dataset is :-  {len(df.index)}")


# b). Data types of columns.

# In[79]:


df.dtypes


# c). Info & describe of data in dataframe.

# In[80]:


df.info


# In[81]:


df.describe


# # 3. Low Level Data Understanding :

# a). Find count of unique values in location column.

# In[82]:


df['location'].nunique()


# b). Find which continent has maximum frequency using values 
# counts.

# In[83]:


df['continent'].value_counts().idxmax()


# c).Find maximum & mean value in 'total_cases'.

# In[84]:


"maximum total cases:",df['total_cases'].max()


# In[85]:


"mean total cases:",df['total_cases'].mean()


# d) Find 25%,50% & 75% quartile value in 'total_deaths'

# In[86]:


"25th percentile value of total deaths:", df['total_deaths'].quantile(0.25)


# In[87]:


"50th percentile value of total deaths:", df['total_deaths'].quantile(0.5)


# In[88]:


"75th percentile value of total deaths:", df['total_deaths'].quantile(0.75)


# e) Find which continent has maximum 
# 'human_development_index'.

# In[89]:


df.groupby('continent')['human_development_index'].max().idxmax()


# f) Find which continent has minimum 'gdp_per_capita'.

# In[90]:


df.groupby('continent')['gdp_per_capita'].max().idxmax()


# # 4. Filter the dataframe with only this columns
# ['continent','location','date','total_cases','total_deaths','gdp_per_ca
# pita','
# human_development_index'] and update the data frame.
# 

# In[91]:


df = df[['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]
df


# # 5. Data Cleaning

#  a) Remove all duplicates observations

# In[92]:


df = df.drop_duplicates()
df


# b) Find missing values in all columns

# In[93]:


df.isnull().sum()


# c)Remove all observations where continent column value is 
# missing

# In[94]:


df=df.dropna(subset=['continent'])
df


# d) Fill all missing values with 0

# In[95]:


df = df.fillna(0)
df


# # 6. Date time format :

#  a) Convert date column in datetime format using 
# pandas.to_datetime
# 

# In[96]:


df['date'] = pd.to_datetime(df['date'])
df


# b)Create new column month after extracting month data from 
# date column

# In[97]:


df['month'] = df['date'].dt.month
df


# # 7. Data Aggregation:
# 

# a) Find max value in all columns using groupby function on 'continent' column

# In[98]:


df_groupby = df.groupby('continent').max().reset_index()
df


# b) Store the result in a new dataframe named 'df_groupby'.

# In[99]:


df=df_groupby
df_groupby


# # 8. Feature Engineering :

# a) Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'

# In[100]:


df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']
df_groupby


# # 9. Data Visualization :
# 

# a) Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.

# In[101]:


sns.distplot(df['gdp_per_capita'],bins = 20 , kde = True )
plt.xlabel('gdp_per_capita')
plt.title('Histrogram and Density plot of GDP per Capita')
plt.show()


# b) Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
# 

# In[102]:


plt.scatter(df_groupby['gdp_per_capita'], df_groupby['total_cases'])
plt.xlabel('Total Casess')
plt.ylabel('GDP Per Capita')
plt.title('plot of total_cases & gdp_per_capita'.upper())


# c) Plot Pairplot on df_groupby dataset.

# In[110]:


plt.show()
df_groupby


# d) Plot a bar plot of 'continent' column with 'total_cases' .

# In[104]:


sns.barplot(x= 'continent', y ='total_cases', data = df_groupby,hue = 'continent')


# # 10.Save the df_groupby dataframe in your local drive using 
# pandas.to_csv function 

# In[106]:


from pathlib import Path  
filepath = Path('Final Project.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df_groupby.to_csv(filepath)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





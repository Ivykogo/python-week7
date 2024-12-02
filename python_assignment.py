#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#Loading the dataset
file_path=r"C:\Users\USER\Downloads\distribution-of-households-growing-other-crops-by-type-county-and-sub-county-2019-census-volume-.csv"
data=pd.read_csv(file_path)


# In[3]:


#Printing out the first five and last five rows
print(data.head())
print(data.tail())


# In[4]:


#Summary of dataset
print(data.info())


# In[5]:


#checking for missing values
print(data.isnull().sum())


# In[5]:


# Fill missing values with the mean for numerical columns (less missing)
columns_fill_mean = ['Farming', 'Maize', 'Camels', 'Pigs', 'Fish Ponds']
for col in columns_fill_mean:
    data[col].fillna(data[col].mean(), inplace=True)


# In[6]:


# Fill moderate missing values with the median
columns_fill_median = ['Sorghum', 'Beans', 'Sweet Potatoes', 'Bananas', 
                       'Potatoes', 'Cabbages', 'Tomatoes', 'Millet', 'Kales',
                       'Ground Nuts','Cassava','Green grams','Watermelons']
for col in columns_fill_median:
    data[col].fillna(data[col].median(), inplace=True)


# In[7]:


# Drop columns with excessive missing values (>50%)
columns_to_drop = ['Cotton', 'Sugarcane', 'Rice', 'Onions','Wheat']
data.drop(columns=columns_to_drop, axis=1, inplace=True)


# In[8]:


print(data.isnull().sum())


# In[9]:


#Checking for duplicates
print(data.duplicated())


# In[10]:


#First five rows after data cleaning
print(data.head(5))


# The dataset is about the distribution of county level agricultural activities in Kenya.
# It includes information on crop production, livestock rearing and aquaculture.
# The data covers a wide range of crops, livestock and fisheries, offering insights into the diversity of agricultural practices across the country.

# In[11]:


## Data analysis
# Descriptive statistics
print(data.describe())


# In[12]:


# Correlations
print(data.corr())


# In[45]:


# Create a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(),annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[19]:


## Data grouping
# Group data by County and calculate total production
county_group = data.groupby('County/Sub County')['Total'].sum()
print(county_group)


# In[18]:


# Group data by County and calculating average livestock production
county_group = data.groupby('County/Sub County')['Livestock Production'].mean()
print(county_group)


# In[25]:


# Visualizing the top 10 counties by total production
# Filter out Kenya
filtered_data = county_group[county_group.index != 'KENYA']

# Visualize the top 10 counties
top_10_counties = filtered_data.sort_values(ascending=False).head(10)
top_10_counties.plot(kind='bar', figsize=(10, 6))
plt.title('Top 10 Counties by Total Production')
plt.xlabel('County/Sub County')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[34]:


# Filter data excluding Kenya
filtered_data = county_group[county_group.index != 'KENYA']

# Sort and get the top 10 counties (excluding Kenya)
top_10_counties = filtered_data.sort_values(ascending=False).head(10)

# Plot the top 10 counties
plt.figure(figsize=(10, 6))
top_10_counties.plot(kind='bar')
plt.title('Top 10 Counties by Average Livestock Production')
plt.xlabel('County/Sub County')
plt.ylabel('Average Livestock Production')
plt.xticks(rotation=45)
plt.show()


# In[48]:


print(data.columns)


# In[49]:


# Histogram of crop production
plt.figure(figsize=(10, 6))
plt.hist(data['Crop Production'], bins=20)
plt.title('Distribution of Crop Production')
plt.xlabel('Crop Production')
plt.ylabel('Frequency')
plt.show()


# In[54]:


# Filter out Kenya
filtered_data = data[data['County/Sub County'] != 'KENYA']

# Bar chart of top 20 counties by total production
top_20_counties = filtered_data.groupby('County/Sub County')['Total'].sum().sort_values(ascending=False).head(20)
plt.figure(figsize=(10, 6))
top_20_counties.plot(kind='bar')
plt.title('Top 20 Counties by Total Production')
plt.xlabel('County/Sub County')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[65]:


# Filter out Kenya and sort by total production (descending)
filtered_data = data[data['County/Sub County'] != 'KENYA'].groupby('County/Sub County')[['Crop Production', 'Livestock Production']].sum().sort_values(by=['Crop Production', 'Livestock Production'], ascending=False).head(10)

# Normalize the data to percentages
filtered_data = filtered_data.div(filtered_data.sum(axis=1), axis=0)

# Create the horizontal bar chart
filtered_data.plot(kind='barh', stacked=True, figsize=(10, 6))
plt.title('Top 10: Crop and Livestock Production')
plt.xlabel('Proportion of Total Production')
plt.ylabel('County/Sub County')
plt.show()


# In[57]:


# Filter out Kenya
filtered_data = data[data['County/Sub County'] != 'KENYA']

# Cumulative sum line chart of total production accross the counties
cumulative_sum = data['Total'].cumsum()

plt.figure(figsize=(10, 6))
cumulative_sum.plot(kind='line')
plt.title('Cumulative Total Production')
plt.xlabel('County/Sub County')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





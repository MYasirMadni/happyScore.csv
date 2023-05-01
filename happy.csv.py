#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df=pd.read_csv('happyscore_income.csv')


# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


# Create a scatter plot of Average Income vs. HappyScore
plt.scatter(df['avg_income'], df['happyScore'])
plt.xlabel('Average Income')
plt.ylabel('HappyScore')
plt.title('Average Income vs. HappyScore')
plt.show()


# In[6]:


# Create a histogram of GDP 
plt.hist(df['GDP'])
plt.xlabel('GDP')
plt.ylabel('Frequency')
plt.title('Histogram of GDP')
plt.show()


# In[7]:


# Create a box plot of Income by Region
df.boxplot(column='avg_income', by='region')
plt.xticks(rotation=90)
plt.title('Income by Region')
plt.show()


# In[8]:


# Create a bar plot of the top 10 countries with highest HappyScore
top_happy = df.sort_values('happyScore', ascending=False).head(10)
plt.bar(top_happy['country'], top_happy['happyScore'])
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('HappyScore')
plt.title('Top 10 countries with highest HappyScore')
plt.show()


# In[9]:


# Create a scatter plot of Income vs. HappyScore with region coloring by matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
for region in df['region'].unique():
    region_df = df[df['region'] == region]
    ax.scatter(region_df['avg_income'], region_df['happyScore'], label=region, alpha=0.7)
ax.set_xlabel('Average Income')
ax.set_ylabel('HappyScore')
ax.set_title('Average Income vs. HappyScore by Region')
ax.legend()
plt.show()


# In[10]:


# Create a scatter plot of Income vs. HappyScore with region coloring
sns.scatterplot(data=df, x='avg_income', y='happyScore', hue='region')
plt.xlabel('Average Income')
plt.ylabel('HappyScore')
plt.title('Average Income vs. HappyScore by Region')
plt.show()


# In[11]:


# Create a violin plot of Income by Region
sns.violinplot(data=df, x='region', y='avg_income')
plt.xticks(rotation=90)
plt.xlabel('Region')
plt.ylabel('Average Income')
plt.title('Income by Region')
plt.show()


# In[12]:


import plotly.express as px
# Create a scatter plot of Income vs. HappyScore with region coloring
fig = px.scatter(df, x='avg_income', y='happyScore', color='region', hover_name='country')
fig.update_layout(title='Average Income vs. HappyScore by Region')
fig.show()


# In[13]:


# Create a bar plot of the top 10 countries with highest HappyScore
fig = px.bar(df.sort_values('happyScore', ascending=False).head(10), x='country', y='happyScore')
fig.update_layout(title='Top 10 countries with highest HappyScore')
fig.show()


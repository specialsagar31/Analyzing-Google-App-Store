#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("C:/Users/speci/Desktop/iNeuron Files/DATA/Google Play Store Apps Dataset/googleplaystore.csv")
df.head()


# # Data Cleaning

# In[7]:


df.info()


# In[26]:


_=df.boxplot()


# In[36]:


df.isnull().sum()


# In[38]:


df[df.Rating>5]


# In[41]:


df.drop([10472],inplace = True)


# In[42]:


df[10470:10475]


# In[43]:


df.boxplot()


# In[45]:


threshold = len(df)* 0.1


# In[46]:


df.dropna(thresh=threshold, axis = 1, inplace = True)


# In[49]:


df.shape


# In[50]:


df['Rating'].fillna(df['Rating'].median(),inplace=True)


# In[51]:


df.isna().sum()


# In[59]:


df["Current Ver"].fillna(str(df["Current Ver"].mode()), inplace = True)
df["Android Ver"].fillna(str(df["Android Ver"].mode()),inplace = True)
df["Type"].fillna(str(df["Type"].mode()),inplace = True)


# In[60]:


df.isna().sum()


# In[68]:


df["Price"] = df["Price"].apply(lambda x: str(x).replace('$','')if '$' in str(x) else str(x))
df["Price"] = df["Price"].apply(lambda x: float(x))
df["Reviews"] = df["Reviews"].apply(lambda x: int(x))
df["Installs"] = df["Installs"].apply(lambda x: str(x).replace('+','')if '+' in str(x) else str(x))
df["Installs"] = df["Installs"].apply(lambda x: str(x).replace(',','')if ',' in str(x) else str(x))
df["Installs"] = df["Installs"].apply(lambda x: float(x))


# In[69]:


df.describe()


# In[71]:


grp = df.groupby("Category")
x = grp['Rating'].agg(np.mean)
y = grp['Reviews'].agg(np.mean)
z = grp['Price'].agg(np.sum)
print(x)
print(y)
print(z)


# # Data Visualization

# In[79]:


plt.figure(figsize = (12,5))
plt.plot(x, 'ro')
plt.title("Category wise Ratings")
plt.xlabel("Categories")
plt.ylabel("Ratings")
plt.xticks(rotation = 90)
plt.show()


# In[84]:


plt.figure(figsize = (12,5))
plt.plot(y, 'ro',color = 'b')
plt.title("Category wise Reviews")
plt.xlabel("Categories")
plt.ylabel("Reviews")
plt.xticks(rotation = 90)
plt.show()


# In[86]:


plt.figure(figsize = (12,5))
plt.plot(z, 'r--',color = 'b')
plt.title("Category wise Prices")
plt.xlabel("Categories-->")
plt.ylabel("Prices-->")
plt.xticks(rotation = 90)
plt.show()


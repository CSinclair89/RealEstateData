#!/usr/bin/env python
# coding: utf-8

# In[127]:


import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import seaborn as sns

pd = pd.read_csv("final_data.csv", engine = "python")
pd


# In[140]:


pd_task1 = pd[["yearbuilt", "totalrooms"]]
pd_task1.dtypes


# In[141]:


pd_task1 = pd_task1[pd_task1["totalrooms"] <= 15]
pd_task1


# In[142]:


task1_x = pd_task1["yearbuilt"]
task1_y = pd_task1["totalrooms"]


# In[143]:


plt.scatter(task1_x, task1_y)


# In[94]:


task1_r = np.corrcoef(task1_x, task1_y)
task1_r


# In[95]:


task1_r2 = task1_r ** 2
task1_r2


# In[99]:


pd_task2 = pd[["lastsoldprice", "bathrooms"]]
pd_task2 = pd_task2[pd_task2["bathrooms"] <= 10]


# In[105]:


task2_x = pd_task2["bathrooms"]
task2_y = pd_task2["lastsoldprice"]
task2_model = st.linregress(task2_x, task2_y)
print(task2_model)


# In[108]:


plt.scatter(task2_x, task2_y)
plt.show()


# In[107]:


task2_r2 = 0.546372 ** 2
task2_r2


# In[122]:


pd_task3 = pd[["finishedsqft", "bedrooms"]]
pd_task3 = pd_task3[(pd_task3["finishedsqft"] < 15000) & (pd_task3["bedrooms"] < 15)]


# In[123]:


task3_x = pd_task3["bedrooms"]
task3_y = pd_task3["finishedsqft"]


# In[135]:


sns.regplot(task3_x, task3_y)


# In[137]:


task3_model = st.linregress(task3_x, task3_y)
print(task3_model)


# In[139]:


task3_r = 0.729854
task3_r2 = task3_r ** 2
task3_r2


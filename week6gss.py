#!/usr/bin/env python
# coding: utf-8

# In[40]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[41]:


pd2 = pd.read_csv("week6gss.csv", engine = "python")
pd2


# In[119]:


pd2 = pd2[pd2["year"] == 1989]
pd2


# In[120]:


pd2.dtypes


# In[131]:


pd2 = pd2[~pd2["hrs2"].str.contains("Inapplicable", "No answer")]
pd2["hrs2"] = pd2["hrs2"].astype(float)
pd2 = pd2.sort_values(by = ["hrs2"])
pd2


# In[132]:


pd2 = pd2[~pd2["income"].str.contains("Do not Know")]
pd2 = pd2[~pd2["income"].str.contains("Refused")]
pd2[['income']] = pd2[['income']].replace('[\$,]','',regex=True)
pd2[['income']] = pd2[['income']].replace('5000 to 5999','5000',regex=True)
pd2[['income']] = pd2[['income']].replace('7000 to 7999','7000',regex=True)
pd2[['income']] = pd2[['income']].replace('10000 to 14999','10000',regex=True)
pd2[['income']] = pd2[['income']].replace('20000 to 24999','20000',regex=True)
pd2[['income']] = pd2[['income']].replace('25000 to mtoe','25000',regex=True)
pd2


# In[133]:


pd2_x = pd2["hrs2"]
pd2_y = pd2["income"]
plt.scatter(pd2_x, pd2_y)
plt.xlabel("Hours worked")
plt.ylabel("Income")
plt.show()


# In[136]:


pd2_r = np.corrcoef(pd2_x, pd2_y)
pd2_r


# In[137]:


pd2_r2 = 0.42615433 ** 2
pd2_r2


# In[139]:


pd2_subset = pd2[["childs", "attend"]]
pd2_subset


# In[150]:


pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Never','0',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Less than once a year','1',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('About once or twice a year','2',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Several times a year','3',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('About once a month','4',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('2-3 times a month','5',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Nearly every week','6',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Every week','7',regex=True)
pd2_subset[["attend"]] = pd2_subset[["attend"]].replace('Several times a week','8',regex=True)
pd2_subset["attend"] = pd2_subset["attend"].astype(float)
pd2_subset["childs"] = pd2_subset["childs"].astype(float)
pd2_subset


# In[153]:


pd2_t2x = pd2_subset["attend"]
pd2_t2y = pd2_subset["childs"]
plt.scatter(pd2_t2x, pd2_t2y)
plt.xlabel("How often they attend religious service?")
plt.ylabel("No. of Children")
plt.show()


# In[154]:


pd2_t2r = np.corrcoef(pd2_t2x, pd2_t2y)
pd2_t2r


# In[155]:


pd2_t2r2 = 0.09666612 ** 2
pd2_t2r2


# In[ ]:





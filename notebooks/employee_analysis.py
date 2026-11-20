#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Introduction
# 
# This notebook analysis employee salary and department information.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("../data/employee18.csv")
df.head()


# # Employee Information
# 
# Displaying employee records and statistical information.

# In[2]:


df.info()


# In[3]:


df.describe()


# # Department Analysis
# 
# Analysing the average salary of each department.

# In[4]:


df.groupby("department")["salary"].mean()


# # Salary analysis
# 
# Displaying the employee salary distribution.

# In[5]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import numpy as np


# # Data Loading from JSON

# In[2]:


a=open('data.json')
data = json.load(a)


# # Social_D_Table

# In[3]:


social_D =pd.DataFrame(data['social_D'])
social_D.head()


# # Price_D_Table
# 

# In[11]:


price_D =pd.DataFrame(data['price_D'])
price_D.head(50)


# # Question 1 
# ### Objective
# #### Aggregation of Specific columns

# # social_D_Aggregation

# In[5]:


social_D.info()


# As we can see overview of each columns including dtype and null values. Since our concerned series is free of null we are not going to implement any null handling approach such as fill_na or drop_na. 

# In[6]:


social_D_agg =social_D[['cumulative_abs','90day_bull_prop_rollingz_60']].agg(["max","min",np.mean])
social_D_agg 


# above is our aggregate fucntions applied on required series. 

# # price_D_Aggregation

# In[7]:


price_D.info()


# In[8]:


price_D_agg = price_D[['last','volume']].agg(["max","min",np.mean])
price_D_agg 


# above is our aggregate functions applied on required series.

# # Question 2 
# ### Objective
# #### Top 3 Highest closing day

# In[18]:


high_price= price_D.sort_values(by='last', ascending= False, ignore_index= True)
top_3_date = high_price['date'].head(3)
top_3_date


# These are the top 3 days when highest last closing happened.

# # Question 3 
# ### Objective
# #### CSV output
# 

# In[41]:


combo = pd.merge(social_D,price_D, on='date' , how= 'inner')
data_col= combo[['date', '90day_bull_prop_rollingz_60', 'cumulative_z', 'last']]
data_col.head()


# In[ ]:


data_col.to_csv('final.csv')


# After merging the two tables social_D and price_D on "date", I have exported the my dataframe in csv. With this I have concluded my task. Thanks 

#!/usr/bin/env python
# coding: utf-8

# ### To begin, I imported the required packages and tested to see the CSV import worked. 

# In[53]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# In[54]:


data = pd.read_csv('./Indicators.csv')


# In[55]:


data.head(10)


# ### After confirming the CSV imported, I began my exploration of the World Indicators data.

# In[57]:


arms_import = 'Arms export'
country = 'USA'

mask1 = data['IndicatorName'].str.contains(arms_import)
mask2 = data['CountryCode'].str.contains(country)
USA_arms = data[mask1 & mask2]


# In[58]:


USA_arms.head(10)


# In[63]:


years = USA_arms['Year'].values
guns = USA_arms['Value'].values

plt.plot( years,guns)
plt.xlabel('Year')
plt.ylabel(USA_arms['IndicatorName'].iloc[0])
plt.title('Arms Exports in the USA 1960-2015')

plt.show()


# ### Next I compared it with the data from the UK

# In[66]:


compare_country = 'GBR'

mask3 = data['IndicatorName'].str.contains(arms_import)
mask4 = data['CountryCode'].str.contains(compare_country)
GBR_arms = data[mask3 & mask4]


# In[68]:


GBR_arms.head()


# In[71]:


years = USA_arms['Year'].values
USA_guns = USA_arms['Value'].values
GBR_guns = GBR_arms['Value'].values

plt.plot( years,USA_guns, label='USA')
plt.plot(years,GBR_guns, label='UK')
plt.xlabel('Year')
plt.ylabel(USA_arms['IndicatorName'].iloc[0])
plt.title('Arms Exports in the USA & UK 1960-2015')

plt.legend()
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## Welcome to the Browser Wars (1995 - )
# <p><img src="https://assets.datacamp.com/production/project_1172/img/browser.png" alt="Browser on desktop, tablet, and phone"></p>
# <p>In the mid 1990s, the First Browser War began with Netscape Navigator and Microsoft Internet Explorer fighting for dominance. By 2001, Internet Explorer was the clear winner, but it was not long before the Second Browser Wars began (2004-2017). This coincided with the rise of smartphones, which emphasized the need and competitiveness for more mobile-friendly versions of browsers. <a href="https://en.wikipedia.org/wiki/Browser_wars">[1]</a></p>
# <p>In this notebook, we'll analyze the worldwide popularity of browsers over time using Google Trends. Although this won't give us direct market share figures, we can use Google Trends to get a sense of interest of a given browser over time and how that interest compares to other browsers. In particular, we will be looking at five major players over the past two decades: Mozilla Firefox (2002-), Apple's Safari (2002-), Google Chrome (2008-), Microsoft Internet Explorer (1995-2020), and Opera (1995-).</p>
# <p>The dataset you will use was downloaded as a CSV from this <a href="https://trends.google.com/trends/explore?date=all&q=%2Fm%2F01dyhm,%2Fm%2F0168s_,%2Fm%2F04j7cyf,%2Fm%2F03xw0,%2Fm%2F01z7gs">Google Trends query</a> in mid-October of 2020. Here are the details:</p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/worldwide_browser_trends.csv</b></div>
# This is a time series indexed by month with the search interest for each browser.
# <ul>
#     <li><b>Month:</b> each month from 2004-01 to 2020-10</li>
#     <li><b>Firefox:</b> search interest for Firefox</li>
#     <li><b>Safari:</b> search interest for Safari</li>
#     <li><b>Google Chrome:</b> search interest for Chrome</li>
#     <li><b>Internet Explorer:</b> search interest for Internet Explorer</li>
#     <li><b>Opera:</b> search interest for Opera</li>
# </ul>
# </div>
# <p>Google defines the values of search interest as:</p>
# <blockquote>
#   <p>Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.</p>
# </blockquote>
# <p>Best of luck and may the best browser win!</p>

# In[27]:


# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd

df = pd.read_csv('datasets/worldwide_browser_trends.csv', 
                 parse_dates=['Month'], index_col='Month')
df.info()


# In[28]:


df.plot()


# In[29]:


df.head(10)


# In[30]:


rolling_six = df.rolling(window=6).mean()
rolling_six.head(20)


# In[31]:


rolling_six.plot()


# In[32]:


df.plot()


# In[33]:


pct_change_quarterly = df.pct_change(3)*100
pct_change_quarterly


# In[34]:


print((20-12)/12)

print(df.head(10))

(33-37)/37


# In[35]:


pct_change_quarterly = pct_change_quarterly.loc['2009':]
pct_change_quarterly.plot(subplots=True, figsize=(12,8))


# In[36]:


chrome_trends = pd.DataFrame()

for year in ['2009', '2012', '2015', '2018']:
    chrome_trends_per_year = df.loc[year, ['Google Chrome']].reset_index(drop=True)
    chrome_trends_per_year.rename(columns={'Google Chrome':year}, inplace=True)
    chrome_trends = pd.concat([chrome_trends, chrome_trends_per_year], axis=1)
    print(chrome_trends)


# In[37]:


chrome_trends.plot()


# In[ ]:





# In[ ]:





# In[ ]:





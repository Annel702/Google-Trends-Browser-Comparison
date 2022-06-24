# Google-Trends-Browser-Comparison
5 Browsers change in popularity since 2004.

In particular, we will be looking at five major players over the past two decades: Mozilla Firefox (2002-), Apple's Safari (2002-), Google Chrome (2008-), Microsoft Internet Explorer (1995-2020), and Opera (1995-).

The dataset you will use was downloaded as a CSV from this Google Trends query in mid-October of 2020. Here are the details:

datasets/worldwide_browser_trends.csv
This is a time series indexed by month with the search interest for each browser.
Month: each month from 2004-01 to 2020-10
Firefox: search interest for Firefox
Safari: search interest for Safari
Google Chrome: search interest for Chrome
Internet Explorer: search interest for Internet Explorer
Opera: search interest for Opera
Google defines the values of search interest as:

Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.


**calculate three key metrics**:

1. Find the six month rolling average for each date and browser in the dataset. 
Save your answer as pandas DataFrame called rolling_six with the column Month as the index. 
Null values are acceptable for dates where a rolling six month average can't be generated.
[Jupyter notebook.pdf](https://github.com/Annel702/Google-Trends-Browser-Comparison/files/8981656/Jupyter.notebook.pdf)


2. Create a DataFrame called pct_change_quarterly with the percentage change from the previous quarter for each date and browser. The values should be in percentage format, so 5 instead of 0.05. Since Chrome launched in late 2008, only include dates during or after 2009.
[Project Comparing Search Interest with Google Trends.pdf](https://github.com/Annel702/Google-Trends-Browser-Comparison/files/8981644/Project.Comparing.Search.Interest.with.Google.Trends.pdf)



3. Even though Chrome eventually overtook Firefox, Chrome's growth has had its fair share of ups and downs.
Illustrate this by comparing Chrome's annual Google Trends performance in 2009, 2012, 2015, and 2018 in a DataFrame called chrome_trends. 
It should hold the search interest for Chrome with four columns for each year and twelve rows for each month of the year.
[Jupyter notebook (autosaved).pdf](https://github.com/Annel702/Google-Trends-Browser-Comparison/files/8981647/Jupyter.notebook.autosaved.pdf)



4. Plot answers
[Plot.pdf](https://github.com/Annel702/Google-Trends-Browser-Comparison/files/8981638/Plot.pdf)




#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[1]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = ''


# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/ ).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# In[2]:


# First, import the relevant modules
import requests
import json
import statistics


# In[3]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
r = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?api_key=yAkdZ-D1QswJiy9SFwyh&start_date=2019-04-22')


# In[4]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
print(r.json())


# #These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[5]:


#Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD)

r = requests.get('https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?api_key=yAkdZ-D1QswJiy9SFwyh&start_date=2017-01-01&end_date=2017-12-31')

print(r.json())


# In[6]:


#2. Convert the returned JSON object into a Python dictionary.

data_dict = r.json()


column_names = data_dict['dataset']['column_names']
#print(column_names)

data = data_dict['dataset']['data']
#print(data)


new_data_dict = {}
for k in column_names:
    new_data_dict[k] = []
    
    
for i in range(len(data)):
    for j in range(len(column_names)):
        new_data_dict[column_names[j]].append(data[i][j])    

print(new_data_dict.keys())    

print("\r")
print(new_data_dict)


# In[7]:


#3. Calculate what the highest and lowest opening prices were for the stock in this period.

print("Max: ", max(x for x in new_data_dict['Open'] if x is not None))

print("Min: ", min(x for x in new_data_dict['Open'] if x is not None))


# In[8]:


#4. What was the largest change in any one day (based on High and Low price)?

new_data_dict['high_diff_low'] = []


for j in range(len(new_data_dict['High'])):
        new_data_dict['high_diff_low'].append(round(new_data_dict['High'][j]-new_data_dict['Low'][j],2))  



print("Max: ", max(x for x in new_data_dict['high_diff_low'] if x is not None))

print("\r")

print("List of values: Difference between High, Low")
print("\r")      
print(new_data_dict['high_diff_low'])


# In[9]:


#5. What was the largest change between any two days (based on Closing Price)?

new_data_dict['diff_prior'] = []

num = len(new_data_dict['Close'])
          
for j in range(num):
    try:
            new_data_dict['diff_prior'].append(round(new_data_dict['Close'][j+1]-new_data_dict['Close'][j],2))  
    except IndexError: 
            new_data_dict['diff_prior'].append(round(new_data_dict['Close'][j-1]-new_data_dict['Close'][j],2))



print("Max Absolute: ", max((abs(x) for x in new_data_dict['diff_prior'] if x is not None)))

print("\r")

print("List of values: Difference between Two Days")
print("\r")      
print(new_data_dict['diff_prior'])


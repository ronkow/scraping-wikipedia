#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wikipedia

# Store the text in the Summary section as a string
text_summary = wikipedia.WikipediaPage(title = 'Yesterday (2019 film)').summary
print(text_summary)


# In[2]:


# Store the text in four other sections as strings
text_plot = wikipedia.WikipediaPage(title = 'Yesterday (2019 film)').section('Plot')
text_cast = wikipedia.WikipediaPage(title = 'Yesterday (2019 film)').section('Cast')
text_release = wikipedia.WikipediaPage(title = 'Yesterday (2019 film)').section('Release')
text_market = wikipedia.WikipediaPage(title = 'Yesterday (2019 film)').section('Marketing')
print(text_cast)


# In[3]:


import pandas as pd

# search for <table> tags and parses all text within the tags
tables = pd.read_html("https://en.wikipedia.org/wiki/Yesterday_(2019_film)")

# print the number of DataFrames in the list
len(tables)


# In[4]:


print(tables[0])


# In[5]:


tables[0].to_csv("infobox_yesterday.csv", index = False)


# In[6]:


import numpy as np

# Create a list for the three string objects
list_yesterday = [text_summary, text_plot, text_cast ]

# Create a list for the column labels of the DataFrame
list_sections = ['Summary', 'Plot', 'Cast']

# Convert the list to a numpy array, and then create the DataFrame
df_yesterday = pd.DataFrame(np.array(list_yesterday).reshape(1,3), columns = list(list_sections))
print(df_yesterday)


# In[7]:


# Create the CSV file
df_yesterday.to_csv('yesterday.csv', sep = ',', index = False)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# search for <table> tags and parses all text within the tags
tables = pd.read_html("https://en.wikipedia.org/wiki/1998_in_film")

# print the number of DataFrames in the list
len(tables)


# In[2]:


df_1998oct = tables[8]
df_1998oct.tail(25)


# In[3]:


# Correct the errors
df_1998oct.loc[26,'Title'] = df_1998oct.loc[26,'Studio']
df_1998oct.loc[26,'Studio'] = df_1998oct.loc[26,'Cast and crew']
df_1998oct.loc[26,'Cast and crew'] = df_1998oct.loc[26,'Genre']
df_1998oct.loc[26,'Genre'] = df_1998oct.loc[26,'Medium']
df_1998oct.loc[26,'Medium'] = df_1998oct.loc[26,'Unnamed: 7']

df_1998oct.loc[27,'Opening.1'] = 25
df_1998oct.loc[27,'Title'] = 'Babe: Pig in the City'

df_1998oct.loc[28,'Opening.1'] = 25
df_1998oct.loc[28,'Title'] = 'Home Fries'

df_1998oct.loc[29,'Opening.1'] = 25
df_1998oct.loc[29,'Title'] = 'Ringmaster'

df_1998oct.loc[30,'Medium'] = df_1998oct.loc[30,'Genre']  
df_1998oct.loc[30,'Genre'] = df_1998oct.loc[30,'Cast and crew']  
df_1998oct.loc[30,'Cast and crew'] = df_1998oct.loc[30,'Studio']  
df_1998oct.loc[30,'Studio'] = df_1998oct.loc[30,'Title']
df_1998oct.loc[30,'Title'] = df_1998oct.loc[30,'Opening.1']  
df_1998oct.loc[30,'Opening.1'] = 25


# In[4]:


df_1998oct.columns


# In[5]:


# Delete the last column
df_1998oct.drop(columns=['Unnamed: 7'], inplace=True)
df_1998oct.tail(25)


# In[6]:


# Concatenate the tables for 1998
df_1998jan = tables[5]
df_1998apr = tables[6]
df_1998jul = tables[7]
df_1998 = pd.concat([df_1998jan, df_1998apr, df_1998jul, df_1998oct])

df_1998.insert(0, 'Year', '1998')
df_1998.head()


# In[7]:


# Concatenate the tables for all years
list_years = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999']

df_1990s = pd.DataFrame()

for year in list_years:
    if year == '1998':
        df_1990s = pd.concat([df_1990s, df_1998])
    else:  
        tables = pd.read_html('https://en.wikipedia.org/wiki/' + year + '_in_film')
        df_jan = tables[5]
        df_apr = tables[6]
        df_jul = tables[7]
        df_oct = tables[8]
        df = pd.concat([df_jan, df_apr, df_jul, df_oct])
        df.insert(0, 'Year', year)
        df_1990s = pd.concat([df_1990s, df])


# In[8]:


len(df_1990s)


# In[9]:


# Rename two columns, reset the row index
df_1990s.rename(columns={'Opening':'Month', 'Opening.1':'Opening Date'}, inplace=True) 
df_1990s.reset_index(inplace=True, drop=True)
df_1990s.tail()


# In[10]:


# Split the data into separate columns
df_genre = df_1990s['Genre'].str.split(',', expand=True)
df_castandcrew = df_1990s['Cast and crew'].str.split(';', expand=True)


# In[11]:


df_genre.tail()


# In[12]:


df_castandcrew.head()


# In[13]:


# Rename the new columns, delete the old columns
df_1990s['Genre1'] = df_genre[0]
df_1990s['Genre2'] = df_genre[1]
df_1990s['Genre3'] = df_genre[2]
df_1990s['Genre4'] = df_genre[3]
df_1990s['Genre5'] = df_genre[4]

df_1990s['Crew1'] = df_castandcrew[0]
df_1990s['Crew2'] = df_castandcrew[1]
df_1990s['Cast1'] = df_castandcrew[2]
df_1990s['Cast2'] = df_castandcrew[3]

df_1990s.drop(columns=['Cast and crew','Genre'], inplace=True)
df_1990s.head()


# In[14]:


# Create the CSV file
df_1990s.to_csv('films_1990s.csv', sep = ',', index = False)


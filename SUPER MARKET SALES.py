#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[1]:


#Getting the details of files in the given directory path
import os
for dirname, _, filenames in os.walk("C:/Users/Pavana Sree/Downloads"):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[4]:


#Reading data into a variable
data = pd.read_csv('C:/Users/Pavana Sree/Downloads/supermarket.csv')


# In[5]:


#Displaying 1st 5 rows
data.head(5)


# In[6]:


#Displaying the count of rows & columns
data.shape


# In[7]:


#Details of each column 
data.info()


# In[8]:


#outputing the statistical values of the data
data.describe()


# In[9]:


#Determining the null values
data.isna().sum()


# In[10]:


#determining the duplicate
data.duplicated().sum()


# In[11]:


#column names
data.columns


# In[12]:


#Determining the data type of column
data.dtypes


# In[13]:


#creating a function for displaying a piechart for the given data
def display_pie_chart(values, labels, title, chart_type = 'pie'):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot()
    if chart_type == 'doughnat':
        explode = np.full(len(labels), 0.05)
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, explode = explode, pctdistance=0.85)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
    else:
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  
    ax.set_title(title)
    
    
    plt.savefig(f'{labels[0]}', bbox_inches='tight')
    plt.show()


# In[14]:


#grouping the columns
def group_by_column(df, col, function):
    grouped_df = df.groupby(col).agg(function).reset_index()
    grouped_df = grouped_df.set_index(col)

    return grouped_df


# In[15]:


#generating piechart differentiated by gender
gender_and_total = data[['Gender', 'Total']]

grouped_by_gender_df = group_by_column(gender_and_total, 'Gender', 'sum')

print(grouped_by_gender_df)

labels = grouped_by_gender_df.index
values = grouped_by_gender_df['Total']

display_pie_chart(values, labels, 'Total Sales by Gender')


# In[16]:


#creating a doughnat piechart based on the customer type
group_by_type = data[['Customer type', 'Total']]

group_by_type_df = group_by_column(group_by_type, 'Customer type', 'sum')

print(group_by_type_df)

labels = group_by_type_df.index
values = group_by_type_df['Total']

display_pie_chart(values, labels, 'Total Sales by Customer type', chart_type = 'doughnat')


# In[17]:


#generating 5 rows of grouped data formed
group = data.groupby(['Product line', 'Gender']).size().reset_index()
group.columns = ['Product line', 'Gender', 'Count']

group.head(5)


# In[18]:


#creating barplot
plt.figure(figsize=(15, 10))


sns.barplot(data=group, x="Product line", y="Count", hue="Gender")
plt.title('Count of Product Line by Gender')
plt.xlabel('Product Line')
plt.ylabel('Count')
plt.savefig('count_by_gender')
plt.show()


# In[19]:


#identifying the cities
data.City.unique()


# In[20]:


#identifying the branches & most selling branch
branches_sales = data.groupby('Branch')['Total'].sum()

for branch, sales in branches_sales.items():
    print(f'Branch {branch} : {sales}')
    
print('-' * 50)

most_selling_branch = branches_sales.idxmax()

print(f'The most selling branch is {most_selling_branch}')


# In[21]:


#creating barchat of total sales in each city
plt.figure(figsize=(10, 6))

branches_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by City')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.show()


# In[22]:


#creating a piechart of average customers differentiated by cities
customer_rate = data.groupby('City')['Rating'].mean()

cities = customer_rate.index
rates = customer_rate

print(customer_rate)

display_pie_chart(rates, cities, 'Avarage Customers Rate by City')


# In[23]:


#Determining the highest selling product
product_sales = data.groupby('Product line')['Quantity'].sum()

highest_selling_product = product_sales.idxmax()

print("Highest selling product:", highest_selling_product)


# In[24]:


#Histogram on sales of each product
plt.figure(figsize=(12, 8))

product_sales.plot(kind='bar',color="pink")
plt.title('Product Sales by Quantity')
plt.xlabel('Product Category',  rotation=0)
plt.ylabel('Quantity')
plt.show()


# In[25]:


#creating a doughnat piechart
grouped_products = data.groupby('Product line')['gross income'].sum()

products = grouped_products.index
income = grouped_products

display_pie_chart(income, products, '', chart_type='doughnat')


# In[26]:


#creating a dataframe
dates = pd.DataFrame()

# Convert Date values in dataset to pd.datetime object
dates['Date'] = pd.to_datetime(data['Date'])

# separate year value form datetime object
dates['Year'] = dates['Date'].dt.year

# separate month value form datetime object
dates['Month'] = dates['Date'].dt.month

# separate day value form datetime object
dates['Day'] = dates['Date'].dt.day

# Get Total column values from the original datafram 
dates['Total'] = data['Total']

dates


# In[27]:


#determining the sales per month
monthly_sales = dates.groupby(['Month', 'Day'])['Total'].sum()

monthly_sales


# In[28]:


#visualization for each month of sales
for month in range(1, 4):
    plt.figure(figsize=(8, 6))
    month_data = monthly_sales.loc[month]
    plt.plot(month_data.index.get_level_values('Day'), month_data.values)
    plt.title(f'Monthly Sales for Month {month}')
    plt.xlabel('Day')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.savefig(f'{month}')
    plt.show()


# In[ ]:





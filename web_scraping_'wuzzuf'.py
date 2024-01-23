# -*- coding: utf-8 -*-
"""Web Scraping 'Wuzzuf'.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-0Cbvl1Xd-Ipc8PvypE8oF-fhKEnXCl

# Importing
"""

!pip install requests
!pip install bs4

import requests
from bs4 import BeautifulSoup
import pandas as pd
import math

"""# Functions"""

jobs = ['machine learning' , 'data analysis' , 'data science' , 'business intelligence']

def number_of_pages(jobName):
  url='https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q='+jobName.replace(' ', '%20')
  response = requests.get(url)
  soup = BeautifulSoup(response.content , 'lxml')
  num_jobs = soup.find('strong').text.replace(',','')
  #print(num_jobs)
  num_pages=math.ceil(int(num_jobs)/15)
  #print(num_pages)
  return num_pages , url

number_of_pages('business intelligence')

def scrap(num_pages , url, job):
  titles_list = []
  links_list = []
  occupations_list =[]
  companies_list =[]
  specs_list =[]
  salaries_list = []
  for i in range (num_pages):
    new_url = url +'&start='+str(i)
    response = requests.get(new_url)
    soup = BeautifulSoup(response.content , 'lxml')

    titles=soup.findAll('h2' , {'class': 'css-m604qf'})
    titles_list+=[title.text for title in titles]

    links_list+=['https://wuzzuf.net'+title.a['href'].replace(' ','')  for title in titles]

    companies=soup.findAll('a',{'class':'css-17s97q8'})
    companies_list+=[company.text.replace(' -' , '') for company in companies]

    occupations=soup.findAll('div',{'class':'css-1lh32fc'})
    occupations_list+=[occupation.text for occupation in occupations]

    specs = soup.findAll('div',{'class':'css-y4udm8'})
    specs_list+=[spec.text.split(' · ') for spec in specs]

  scraped_data={}
  for j in range(len(titles_list)):
      scraped_data['job Name'] = job
  scraped_data['Title'] = titles_list
  scraped_data['Company'] = companies_list
  scraped_data['Occupation'] = occupations_list
  scraped_data['Specs'] = specs_list
  scraped_data['Link'] = links_list

  df = pd.DataFrame(scraped_data)
  display(df)
  return df

combined_df = pd.DataFrame()
for job in jobs:
    pages, URL = number_of_pages(job)
    df = scrap(pages, URL, job)
    combined_df = pd.concat([combined_df, df])
    combined_df.reset_index(drop=True, inplace=True)
display(combined_df)

combined_df.to_csv('JobScraping.csv', index=False)
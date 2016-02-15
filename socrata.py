# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 12:57:07 2016

@author: wiconnelly
"""

import pandas as pd
import numpy as np

va_data_2010_Q4 = pd.read_csv("C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/2010_Q4.csv")
va_data_2011_Q4 = pd.read_csv("C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/2011_Q4.csv")
va_data_2012_Q4 = pd.read_csv("C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/2012_Q4.csv")
va_data_2013_Q4 = pd.read_csv("C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/2013_Q4.csv")
va_data_2014_Q3 = pd.read_csv("C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/2014_Q3.csv")

va_data_2014_Q3['FY'] = '2014'
va_data_2014_Q3['QTR'] = '3'

va_data_2013_Q4['FY'] = '2013'
va_data_2013_Q4['QTR'] = '4'

va_data_2012_Q4['FY'] = '2012'
va_data_2012_Q4['QTR'] =  '4'

va_data_2011_Q4['FY'] = '2011'
va_data_2011_Q4['QTR'] = '4'

va_data_2010_Q4 ['FY'] = '2010'
va_data_2010_Q4 ['QTR'] = '4'

va_data_dict = {'2010': va_data_2010_Q4,'2011': va_data_2011_Q4, '2012':va_data_2012_Q4, 
'2013': va_data_2013_Q4, '2014': va_data_2014_Q3 }

VA_data = pd.concat(va_data_dict)

VA_data.FY = VA_data.FY.astype(int)

    
    
VA_data.to_csv('C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/va_data.csv')


# ------- #

va_data = pd.read_csv("https://raw.githubusercontent.com/wbconnelly/Second_Repo_Aug_20/master/va_data.csv", header = 0)


city = []
for i in va_data.LOCATION:
    x =""    
    if i.find(",") == -1:
        x = i
    else: 
        x = i[:i.find(',')]
    city.append(x)

va_data['City'] = city

state = []
for i in va_data.LOCATION:
    x =""    
    if i.find(",") == -1:
        x = i
    else: 
        x = i[i.find(',') + 1: i.find('(')].strip(" ")
    state.append(x)

va_data['State'] = state

City_State = []
for i in va_data.LOCATION:
    x =""    
    if i.find(",") == -1:
        x = i
    else: 
        x = i[: i.find('(')].strip(" ")
    City_State.append(x)

va_data['City_State'] = City_State

State2 = []
for i in va_data.City_State:
    x =""    
    if i.find(",") == -1:
        x =  i[:i.find('(')].strip(" ")
    else: 
        x = i[i.find(',')+1:].strip(" ")
    State2.append(x)
va_data['State'] = State2

state2 = []
for i in va_data['State']:
    x = i.replace('Central ', '')
    y = x.replace('Eastern ','')
    z = y.replace('Southern ','')
    w = z.replace('Northern ', '')
    s = w.replace('Western ', '')
    e = s.replace('North ', '')
    r = e.replace('South ', '')
    j = r.replace('East ', '')    
    p = j.replace('West ', '')
    v = p.replace(' Harbor - Brooklyn', '')
    v = v.replace(' Harbor', '')
    state2.append(v)
    
va_data['State'] = state2

pct_asp = []
for i in va_data.NOTES:
    if i.find('%') != -1:
        x = int(i[i.find('%') - 2: i.find('%')])
    elif'value meets or exceeds aspirational goal; ' in i:
        x = 100
    else:
        x = ''
    pct_asp.append(x)
    
va_data['pct_asp_wn'] = pct_asp
    
set(pct_asp)

state = []
for i in va_data.State:
    if i == 'Connecticut':
        x = 'CT'
    elif i == 'New York':
        x = 'NY'
    elif i == 'New Jersey':
        x = 'NJ'
    elif i == 'Maryland':
        x = 'MD'
    elif i == 'Indiana':
        x = 'IN'
    elif i == 'Arkansas':
        x = "AR"
    elif i == 'New Mexico':
        x = 'NM'
    elif i == 'Arizona':
        x = 'AZ'
    elif i == 'Montana':
        x = 'MT'
    elif i == "Colorado":
        x = 'CO'
    elif i == 'Alaska':
        x = 'AK'
    elif i == 'Sierra Nevada':
        x = 'CA'
    elif i == 'Alabama':
        x = 'AL'
    elif i == 'California':
        x = 'CA'
    elif i == 'Texas':
        x = 'TX'
    elif i == 'IL / IN':
        x = 'IL'
    else:
        x = i
    state.append(x)

va_data['State'] = state

va_data.head()

va_data['City_State'] = va_data['City'] + ', ' + va_data['State']

va_data.State.unique()

va_data.pct_asp_wn

va_data.to_csv('C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/VA_DATA_V2.csv')
va_data_2010 = va_data[va_data.FY == 2010]

va_data_2010.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/va_data_2010.csv')

va_data2 = va_data.ix[:, 2:]

measure_cat = []
for i in va_data2.MEASURE:
    x = i[: i.find(" ")]
    measure_cat.append(x)
va_data2['MEASURE_CATEGORY'] = measure_cat

measure_def = []
for i in va_data2.MEASURE:
    x = i[i.find(" ", i.find(" ") +1):].strip()
    measure_def.append(x)
va_data2['MEASURE_DEF'] = measure_def
va_data2['pct_asp_wn'] = pct_asp

va_data2.head()

va_data2.columns
# get the Averages across years for all States


va_data2['pct_asp_wn'].mean()
x = va_data2.pct_asp_wn
PCT_ASP = x.convert_objects(convert_numeric= True)
# or 
va_data2['pct_asp_wn'] = va_data2['pct_asp_wn'].astype('float')

va_data2['pct_asp_wn'] = list(PCT_ASP)
va_data2['pct_asp_wn'].mean(dropna = True)


va_data2.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/VA_DATA_V2.csv')

# Get averages for each value grouped by State and Fiscal Year
va_data2.groupby(['State', 'FY']).mean().reset_index()

st_ct = va_data2.groupby(['FACILITY', 'State']).count().reset_index()

State_count = st_ct.State.value_counts().reset_index()
State_count['State_ABB'] = State_count['index']
State_count['Facility_Count'] = State_count[0]
State_count = State_count[['State_ABB', 'Facility_Count']]

# read in the number of veterans by state
vets_st = pd.read_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/vets_state.csv')


Vets_Stats = pd.merge(State_count, vets_st, on = 'State_ABB')
Vets_Stats.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/Vets_Stats.csv')
Vets_Stats =  pd.read_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/Vets_Stats.csv')

Vets_Stats['Facilities_per_Capita'] = Vets_Stats['Total Vets'] / Vets_Stats['Facility_Count']

Vets_Stats['Total Vets'] = Vets_Stats['Total Vets'].astype('float')
Vets_Stats.describe()

va_data2.dropna().groupby(['State','MEASURE_CATEGORY', 'FY']).mean().reset_index()
va_data2.dropna(how = 'all').groupby(['State','MEASURE_CATEGORY']).mean().reset_index()
va_avg_state_cat = va_data2.dropna(how = 'all').groupby(['MEASURE_CATEGORY', 'State']).mean().reset_index()

va_avg_yr_state_cat = va_data2.dropna(how = 'all').groupby(['FY', 'State','MEASURE_CATEGORY']).mean().reset_index()


va_avg_yr_state_cat.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/AVG_ST_YR_CAT.csv')
va_avg_state_cat.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/AVG_ST_CAT.csv')

va_avg_cat_col = pd.read_csv('C:\Users\wiconnelly\Desktop\DSA_Homework_VA_ASPIRE_data\AVG_ST_YR_CAT_pivot.csv')
va_cat_col = va_avg_cat_col[['State', 'State Name', 'MEASURE_CATEGORY','Improvement 10-14' ]]

va_cat_col = pd.pivot_table(va_cat_col , values='Improvement 10-14', index='State Name', columns=['MEASURE_CATEGORY'])


va_cat_col.to_csv('C:\Users\wiconnelly\Desktop\DSA_Homework_VA_ASPIRE_data\category_columns_improvement_allyrs.csv')


# find average scores by facility in each state

va_data_fac = va_data2[['FACILITY', 'City', 'State', 'City_State', 'MEASURE_CATEGORY', 'SCORE', 'FY']]
va_data_fac.groupby(['FACILITY', 'City', 'State', 'MEASURE_CATEGORY',  'FY']).mean().reset_index()
va_data_fac_pivot = pd.pivot_table(va_data_fac , values='SCORE', index=['FACILITY','City', 'State', 'MEASURE_CATEGORY'], columns='FY')
va_data_fac_pivot.to_csv('C:/Users/wiconnelly/Desktop/DSA_Homework_VA_ASPIRE_data/va_data_fac_pivot.csv')













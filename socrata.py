
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
        x = i[i.find('%') - 2: i.find('%')]
    elif'value meets or exceeds aspirational goal; ' in i:
        x = 100
    else:
        x = 'nan'
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

va_data_2010.to_csv('C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/va_data_2010.csv')

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


va_data2.head()

va_data2.to_csv('C:/Users/William/Desktop/DSA_Homework_VA_ASPIRE_data/VA_DATA_V2.csv')

va_data2.columns
# get the Averages across years for all States
va_data2.groupby(['State', 'FY']).mean().reset_index()



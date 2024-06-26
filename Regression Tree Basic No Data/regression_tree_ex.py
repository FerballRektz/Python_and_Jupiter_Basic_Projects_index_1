import pandas as pd 
import numpy as np 
import statistics as st

"""code by Gerard Irao"""
data = {
'Sample':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
'Sex': ['M', 'F' ,'M' ,'M' ,'F' ,'F' ,'M','M','M','F','F','M','F','M','F'],
'EconStat': ['High','High','Low','High','High','Low','High','Low','High','High','Low','Low','High','Low','Low'],
'Employment': ['Private','Public','Private','Public','Private','Private','Private','Public','Private','Public','Public','Public','Public','Public','Private'],
'Age': [45,40,42,43,38,55,35,27,43,41,43,29,39,55,19]
}




df = pd.DataFrame(data)
dfsex = df.groupby('Sex').agg({'Age' : ['count',st.pstdev]})
dfecon = df.groupby('EconStat').agg({'Age' : ['count',st.pstdev]})
dfemp = df.groupby('Employment').agg({'Age' : ['count',st.pstdev]})
print(df)
print("\n")
print(st.pstdev(df['Age']))
print('\n')
print(dfsex)
print('\n')
print(dfecon)
print('\n')
print(dfemp)

# information gain equation for each category 
calsex = 9.185495813146579 - ((7/15)*(9.837454)+(8/15)*(8.565009))
calecon = 9.185495813146579 -((8/15)*(3.000000)+(7/15)*(12.981934))
calemp = 9.185495813146579 -((7/15)*(10.224021)+(8/15)*(8.169111))

newdf = {
 "Name": ["Sex","Economic Status","Employment"],   
 "Values": [calsex,calecon,calemp]
}
print("\n")    
print(pd.DataFrame(newdf))


dfprivh = df.loc[(df['Employment']=='Private') & (df['EconStat'] == 'High')]
dfpubh = df.loc[(df['Employment']=='Public')& (df['EconStat'] == 'High')]
dfprivl = df.loc[(df['Employment']=='Private') & (df['EconStat'] == 'Low')]
dfpubl = df.loc[(df['Employment']=='Public')& (df['EconStat'] == 'Low')]
dfprivm = df.loc[(df['Sex']=='M') & (df['EconStat'] == 'High')]
dfprivf = df.loc[(df['Sex']=='F')& (df['EconStat'] == 'High')]
dfpubm = df.loc[(df['Sex']=='M') & (df['EconStat'] == 'Low')]
dfpubf = df.loc[(df['Sex']=='F')& (df['EconStat'] == 'Low')]
print("\n")
print('The calculations of high economic status employees')
print('Public')
print(st.pstdev(dfpubh['Age']))
print('Private')
print(st.pstdev(dfprivh['Age']))
print('\n')
print('The calculations of low economic status employees')
print('Public')
print(st.pstdev(dfpubl['Age']))
print('Private')
print(st.pstdev(dfprivl['Age']))
print("\n")
print("males")
print(st.pstdev(dfpubm['Age']))
print(st.pstdev(dfprivm['Age']))
print('Female')
print(st.pstdev(dfpubf['Age']))
print(st.pstdev(dfprivf['Age']))
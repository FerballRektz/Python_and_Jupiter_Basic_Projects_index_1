import pandas as pd 
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv('Zeta_export\\Basic\\COVID19 Basic EDA\\COVID19 2021.csv')
"""
Age              int64
Sex             object
RegionRes       object
HealthStatus    object
Days             int64

"""

df12 = df.loc[df['DateOnset'].str.contains('^(1|2)\/\d\/2021',regex= True)]
df34 = df.loc[df['DateOnset'].str.contains('^(3|4)\/\d\/2021',regex= True)]
df56 = df.loc[df['DateOnset'].str.contains('^(5|6)\/\d\/2021',regex= True)]
df78 = df.loc[df['DateOnset'].str.contains('^(7|8)\/\d\/2021',regex= True)]
df910 = df.loc[df['DateOnset'].str.contains('^(9|10)\/\d\/2021',regex= True)]
df1112 = df.loc[df['DateOnset'].str.contains('^(11|12)\/\d\/2021',regex= True)]


#finding case per day 
dfcase = df.groupby('DateOnset')['Days'].count()
print(dfcase.sort_values(ascending= False))


#date plot

df12 = df.loc[df['DateOnset'].str.contains('^(1|2)\/\d\/2021',regex= True)].count()[0]
df34 = df.loc[df['DateOnset'].str.contains('^(3|4)\/\d\/2021',regex= True)].count()[0]
df56 = df.loc[df['DateOnset'].str.contains('^(5|6)\/\d\/2021',regex= True)].count()[0]
df78 = df.loc[df['DateOnset'].str.contains('^(7|8)\/\d\/2021',regex= True)].count()[0]
df910 = df.loc[df['DateOnset'].str.contains('^(9|10)\/\d\/2021',regex= True)].count()[0]
df1112 = df.loc[df['DateOnset'].str.contains('^(11|12)\/\d\/2021',regex= True)].count()[0]

plt.title('Number of COVID19 cases in months')
plt.ylabel('Number of cases')
plt.xlabel('Months')
plt.plot(['Jan-Feb','Mar-Apr','May-Jun','Jul-Aug','Sep-Oct','Nov-Dec'],[df12,df34,df56,df78,df910,df1112])






#count of female and male

df_f = df.loc[df['Sex'] == 'FEMALE'].count()[0]
df_m = df.loc[df['Sex'] == 'MALE'].count()[0]
df_fage = df.loc[(df['Sex'] == 'FEMALE') & (df['HealthStatus']=='DIED')].count()[0]
df_mage = df.loc[(df['Sex'] == 'MALE') & (df['HealthStatus']=='DIED')].count()[0]
fig, ax = plt.subplots(2,1, figsize = (10,10))
genders = ['Female','Male']
ax[0].set_title('Infectivity of COVID 19 in Relation to Gender')
ax[0].set_ylabel('Number of Cases')
ax[0].bar(genders,[df_f,df_m], width = 0.4 )
ax[1].set_title('Mortality of COVID 19 in Relation to Gender')
ax[1].set_ylabel('Number of Deaths')
ax[1].bar(genders,[df_fage,df_mage], width = 0.4)
plt.show()


#Average COVID 19 Recovery Between Age Groups (2021)
dfchild = df.loc[(df['Age'] >= 0) & (df['Age'] <= 13)]
dfteen = df.loc[(df['Age'] > 13) & (df['Age'] <= 25)]
dfadult = df.loc[(df['Age'] > 25) & (df['Age'] <= 61)]
dfpresen = df.loc[(df['Age'] > 61) & (df['Age'] <= 73)]
dfsen = df.loc[(df['Age'] > 73) & (df['Age'] <= df['Age'].max()+1)]
dfcdmean = dfchild['Days'].mean()
dftnmean = dfteen['Days'].mean()
dfatmean = dfadult['Days'].mean()
dfpnmean = dfpresen['Days'].mean()
dfsnmean = dfsen['Days'].mean()
df_agev =[dfcdmean,dftnmean,dfatmean,dfpnmean,dfsnmean]
df_lab = ['Child','Teen','Adult','Pre-Senile','Senile']
plt.bar(df_lab,df_agev)
plt.title('Average COVID 19 Recovery Between Age Groups (2021)')
plt.ylabel('Days of recovery')
plt.xlabel('Age')
plt.show()



#GenderMean
df_f = df.loc[df['Sex'] == 'FEMALE']
df_m = df_f = df.loc[df['Sex'] == 'MALE']
df_fdays = df_f = df.loc[df['Sex'] == 'FEMALE']['Days'].mean()
df_mdays = df_f = df.loc[df['Sex'] == 'MALE']['Days'].mean()
plt.bar(['Female','Male'],[df_fdays,df_mdays])
plt.title('Average Recovery Between Genders')
plt.ylabel('Average Recovery')
plt.xlabel('Gender')
plt.show()
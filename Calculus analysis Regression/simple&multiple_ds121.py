# import libraries
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.api as sm


initial_df = pd.read_excel("Zeta_export\\Basic\\Calculus analysis Regression\\CALCULUS GRADE.xlsx")
cleaned_df = initial_df.fillna(value=0)
final_df = cleaned_df.sample(n=100)
# look at each df 
print("initial df \n")
print(initial_df)
print("cleaned df \n")
print(cleaned_df)
print("final df \n")
print(final_df)




#creating variables for linear regression
final_df["intercept"]= 1
y = final_df["Final_Standing"]
x_1 = final_df[["EnTest_M","intercept"]]
x_2 =final_df[["Test1","intercept"]]
x_3 =final_df[["Test2","intercept"]]
x_4 =final_df[["Test3","intercept"]]
x_5 =final_df[["Test4","intercept"]]
xs =[x_1,x_2,x_3,x_4,x_5]

#multiple simple linear
for i in xs:
    mod = sm.OLS(y,i)
    fii = mod.fit()
    coef = fii.summary2().tables[1]["Coef."][0]
    inter = fii.summary2().tables[1]["Coef."][1]
    lrr1 = fii.summary2().tables[0][1][6]
    regpvalue = fii.summary2().tables[1]["P>|t|"][0]
    intpvalue = fii.summary2().tables[1]["P>|t|"][1]
    name = i.columns.values
    print(f"\nregression equation of {name[0]} = {coef}*x+{inter}\n"
          f"R^2 = {lrr1} \n"
          f"pvalue ={regpvalue}")


    



# multiple linear regression
index_i = final_df.columns.values.tolist()
remove = ['Sex', 'Course', 'INCOME', 'MU_SHS?', 'Final_Standing', 'Pass-Fail', 'Final_Grade']
x2= final_df.drop(remove,axis=1)
mod2 = sm.OLS(y,x2)
fii2 = mod2.fit()
finaldata2 = fii2.summary2().tables[1]
coeflist2=[]
regp2 =[]
for i in range(6):
   coef2 = fii2.summary2().tables[1]["Coef."][i]
   regpvalue2 = fii2.summary2().tables[1]["P>|t|"][i]

   coeflist2.append(coef2)
   regp2.append(regpvalue2)
lrr2 = fii2.summary2().tables[0][1][6]
print(f"\n\nMultiple Regression Equation = {coeflist2[0]}*x_1+{coeflist2[1]}*x_2 + {coeflist2[2]}*x_3+{coeflist2[3]}*x_4+{coeflist2[4]}*x_5+{coeflist2[5]}\n"
f"\nR={lrr2}\n"
f"pval={regp2}\n\n")


#remove insignificant values

x3= x2.drop("EnTest_M",axis=1)
mod3 = sm.OLS(y,x3)
fii3 = mod3.fit()
finaldata3 = fii3.summary2().tables[1]
coeflist3=[]
regp3 =[]
for i in range(5):
   coef3 = fii3.summary2().tables[1]["Coef."][i]
   regpvalue3 = fii3.summary2().tables[1]["P>|t|"][i]

   coeflist3.append(coef3)
   regp3.append(regpvalue3)
lrr3 = fii3.summary2().tables[0][1][6]
print(f"\n\nModified Multiple Regression Equation = {coeflist3[0]}*x_2 + {coeflist3[1]}*x_3+{coeflist3[2]}*x_4+{coeflist3[3]}*x_5+{coeflist3[4]}\n"
f"\nR={lrr3}\n"
f"pval={regp3}\n\n")

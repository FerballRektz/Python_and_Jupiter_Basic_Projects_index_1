# Calculus Grade Regression Analysis

## I. Objective
perform regression analysis using python in Calculus Grade data
## II. Scope
The project will perform these types of regression analysis only:
- linear regression analysis
- multiple regression analysis

## III. Data used 
the data is obtained from Mapua Mathematics Department data, important student data is omitted other than the student sex and student name. The data is composed of the ff: <br>
Sex = char, biological sex of the student <br>
Course = string, course enrolled by the student  <br>
INCOME = int, levels where it represents income brackets [no data on what each level represents what]<br>
MU_SHS? = string, if one enrolled in Mapua University in Senior High School  <br>
EnTest_M = int,  calculus final examination test<br>
Test1,Test2,Test3,Test4 = float, calculus exam test grades  <br>
Final_Standing = float, grade of the student in calculus course <br>
Pass-Fail = char, if the student pass(P) or not(F)  <br>
Final_Grade = numerical grade representation of the student course outcome<br>
## IV. How the code is done
The project is done through 5 code blocks, these code blocks are: <br>
1. Data Preprocessing <br>
    - missing data is filled with 0 and 100 random rows are obtained  

2. Multiple simple linear regression  
    - creating multiple simple linear models based from EnTest_M,Test1,Test2,Test3,Test4 as x and y as the Final_Standing  

3. Multiple linear regression  
    - creating multiple linear model based from EnTest_M,Test1,Test2,Test3,Test4 as x and y as the Final_Standing  

4. Removal of residuals for multiple linear regression  
    - removing insignificant x in multiple regression model  

## V. Results 
it shows the relationship and how x explains y of the test and its final standing. it is found that the model that has a high R is the unmodified multiple regression model

## VI. Code and Project Reccomendations
there is both code and project reccomendations that needs to be addressed:
1. There should be a more efficent way to do multiple regression model and residual removal in one block of code
2. there should be plots or interactive graphs showing the regression model

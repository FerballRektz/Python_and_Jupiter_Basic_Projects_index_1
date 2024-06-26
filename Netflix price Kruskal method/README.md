# Using Kruskal Method to Determine Netflix Price Variance for Developed and Developing Countries
##  I. Objective
to know if there is a variance difference between netflix prices in developing and developed countries
## II. Scope
the data in determining if the country is developing or is a developed country is the use of the GINI index. According to the World Bank, GINI index measures the **extent to which the distribution of income or consumption among individuals or households within an economy deviates from a perfectly equal distribution**. A Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality. To know more [Click Here](https://databank.worldbank.org/metadataglossary/gender-statistics/series/SI.POV.GINI#:~:text=Gini%20index,of%20100%20implies%20perfect%20inequality.)

## III. Data used 
The data used in this project is based from the two following sources: <br>
[Netflix subscription fee in different countries](https://kaggle.com/datasets/prasertk/netflix-subscription-price-in-different-countries?select=netflix+price+in+different+countries.csv)  <br>
[World Bank Gini Index](https://data.worldbank.org/indicator/SI.POV.GINI)

## IV. How the code is done
In completing the objective (based on the limits also of the scope), the project can be divided into three blocks of code that has specific processes:
###  I. Data Pre-processing
the two data in the datasets in combined to identify developed countries to developing countries
### II. Showing Variances of Netflix prices between developed and developing 
A specific parameter is then used to determine in what gini ranges contitute a developed country and a  developing country to categorize the data, the project used **gini = 32** in those that is lower than the specified **gini** is a developed country and those equal or higher is a developing country  

after categorizing the data, the  Netflix price variances and count is calculated per category    

### III. Validity Testing of variance difference using Kruskal Method 
Upon knowing the variances between each category of countries, it is **essential to know if the differences between the countries is significant.** The [ Kruskal-Wallis H-test for independent samples](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html) is used to determine if there is really a difference of prices between categories

## V. Result Summary
The result shows varying price variance between developing and developed countries, it shows that the variance of developed countries is lower than developing countries indicating that the distribution of developed countries is less distributed compared to developing countries. It also shows that differences between the variance of each category is **significant** (p ${\le}$ 0.05) 

## VI. Code and Project Reccomendation
there is both code and project reccomendations that needs to be addressed: <br>
1. There needs to be more factors in determining what country constitutes to a developed and developing country
2. There should be better visualisation in showing the variance between each price
3. There should be a more indepth analysis on the mean of developed countries in relation to its variance to know if its average is more higher compared to developing countries




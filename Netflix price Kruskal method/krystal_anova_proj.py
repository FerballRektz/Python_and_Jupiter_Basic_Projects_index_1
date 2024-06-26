from scipy.stats import kruskal
import numpy as np
import pandas as pd



def main():
  
  # read files
  country_df = pd.read_csv("Zeta_export\\Basic\\Netflix price Kruskal method\\netflix_price_in_different_countries.csv")
  gini_df = pd.read_csv("Zeta_export\\Basic\\Netflix price Kruskal method\\gini_by_country.csv")
  # show each data 
  print("COUNTRIES:\n",country_df.head(n =2))
  print("GINI:\n",gini_df.head(n = 2))
  
  
  
  #  I. Data pre-processing 
  gini_df_countries = country_df["Country"]
  # get latest gini index data 
  gini_value = list()
  gini_year_value = list()
  gini_countries = list()
  gini_basic_cost = list()
  gini_standard_cost = list()
  gini_premium_cost = list()

  #create dataframe map for latest gini data per country 
  for i in gini_df_countries:
      country_chosen = gini_df[gini_df["country_name"] == i].reset_index(drop = True)
      
      country_chosen_length = len(country_chosen)      
      if country_chosen_length == 0:
          continue
      else:
          country_chosen_length-=1

      latest_country_data = country_chosen.iloc[country_chosen_length,:]
      gini_countries.append(latest_country_data.loc["country_name"])
      gini_value.append(latest_country_data.loc["value"])
      gini_year_value.append(latest_country_data.loc["year"])

      country_df_cost_data = country_df[country_df["Country"] == i].reset_index(drop = True)
      gini_basic_cost.append(country_df_cost_data.loc[0,"Cost Per Month - Basic ($)"])
      gini_standard_cost.append(country_df_cost_data.loc[0,"Cost Per Month - Standard ($)"])
      gini_premium_cost.append(country_df_cost_data.loc[0,"Cost Per Month - Premium ($)"])
      


  gini_df_latest_only = pd.DataFrame({"country_name": gini_countries , "latest_year": gini_year_value, "gini": gini_value,"Cost Per Month - Basic ($)":gini_basic_cost,
                                     "Cost Per Month - Standard ($)": gini_standard_cost,"Cost Per Month - Premium ($)": gini_premium_cost})
  print("FINAL DATAFRAME:\n",gini_df_latest_only.head(n =2))


  #  II. Showing Variances between developing and developed
  gini_range = 32 # 
  df_developed= gini_df_latest_only[gini_df_latest_only["gini"] < gini_range]
  df_not_developed = gini_df_latest_only[gini_df_latest_only["gini"] >= gini_range]
  print("developed")
  print("Basic",np.var(df_developed["Cost Per Month - Basic ($)"]))
  print("Standard",np.var(df_developed["Cost Per Month - Standard ($)"]))
  print("Premium",np.var(df_developed["Cost Per Month - Premium ($)"]))
  print("Count",df_developed["Cost Per Month - Basic ($)"].count())
  print("Not developed")
  print("Basic",np.var(df_not_developed["Cost Per Month - Basic ($)"]))
  print("Standard",np.var(df_not_developed["Cost Per Month - Standard ($)"]))
  print("Premium",np.var(df_not_developed["Cost Per Month - Premium ($)"]))
  print("Count", df_not_developed["Cost Per Month - Basic ($)"].count())
  
  
  # FINDINGS: different variance and count so  we are gonna use krustal method
  
  
  # III. Kruskal Calculations for validility testing
  print("\n\n Krustal method calculations \n")
  print("\nStandard\n")
  dfdevbas = df_developed["Cost Per Month - Basic ($)"]
  dfndevbas = df_not_developed["Cost Per Month - Basic ($)"]
  kvalbas = kruskal(dfdevbas,dfndevbas)
  print(kvalbas)
  print("\nStandard\n")
  dfdevstd = df_developed["Cost Per Month - Standard ($)"]
  dfndevstd = df_not_developed["Cost Per Month - Standard ($)"]
  kvalstd = kruskal(dfdevstd,dfndevstd)
  print(kvalstd)
  print("\nPremium\n")
  dfdevpre = df_developed["Cost Per Month - Premium ($)"]
  dfndevpre = df_not_developed["Cost Per Month - Premium ($)"]
  kvalpre = kruskal(dfdevpre,dfndevpre)
  print(kvalpre)

if __name__ == "__main__":
  main()
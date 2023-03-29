## Import library
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go
from datetime import datetime, timedelta

## function
def get_year_list(n, start_date):
    year_list = []
    year = start_date.year

    if n <= 0:
        return year_list
    else:
        for i in range(n):
            year_list.append(year+i)

    return year_list

class MyInvesment:

    def __init__(self, capital, interest_rate):
        self.capital = capital
        self.interest_rate = interest_rate

    def get_profit(self, n_year):
        profit = self.capital*((self.interest_rate+1)**(n_year)) - self.capital

        return profit

    def get_new_capital(self, n_year):
        new_capital = self.capital*((self.interest_rate+1)**(n_year))

        return new_capital

## Input
folder = os.getcwd()
print(f'your current folder is {folder}')
file = r'sample.csv'
file_dir = os.path.join(folder,file)
df = pd.read_csv(file_dir)

n_year = 10
start_date = datetime.now()
start_year = start_date.year
list_year = get_year_list(n_year, start_date)

## Execution
df1 = {
    "Investment portfolio": [],
    "Interest rate": [],
    "Capital": [],
    "Year": [],
    "Profit": [],
    "New Capital": []
}

for i in range(len(df["Investment portfolio"])):
    my_invesment = MyInvesment(df["Capital"][i], df["Interest rate"][i])

    for j in range(n_year):
        df1["Investment portfolio"].append(df["Investment portfolio"][i])
        df1["Interest rate"].append(df["Interest rate"][i])
        df1["Capital"].append(df["Capital"][i])
        df1["Year"].append(list_year[j])
        df1["Profit"].append(np.round(my_invesment.get_profit(list_year[j]-start_year)))
        df1["New Capital"].append(np.round(my_invesment.get_new_capital(list_year[j]-start_year)))

df2 = pd.DataFrame(df1)
df3 = df2.groupby( ['Year'], dropna=False, as_index=False).agg( Total_Profit = ('Profit','sum'), AVG_Profit = ('Profit','mean'), Total_Capital = ('New Capital','sum') )
df3['AVG_Profit'] = df3['AVG_Profit'].round(2)

## Save file
df2.to_csv('summary_Invesment_by_Portfolio.csv', index=False)
df3.to_csv('summary_Invesment_by_Year.csv', index=False)
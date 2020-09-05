import pandas as pd

url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/cases_timeseries_prov.csv"
df = pd.read_csv(url,index_col=0,parse_dates=[0])

print(df.head(5))


import pandas as pd

cases_url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/cases_timeseries_prov.csv"
cases_data = pd.read_csv(cases_url,index_col=0,parse_dates=[0])
qc_cases_data = cases_data.loc["Quebec"]

mortality_url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/mortality_timeseries_prov.csv"
mortality_data = pd.read_csv(mortality_url,index_col=0,parse_dates=[0])
qc_mortality_data = mortality_data.loc["Quebec"]

recovered_url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/recovered_timeseries_prov.csv"
recovered_data = pd.read_csv(recovered_url,index_col=0,parse_dates=[0])
qc_recovered_data = recovered_data.loc["Quebec"]

testing_url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/testing_timeseries_prov.csv"
testing_data = pd.read_csv(testing_url,index_col=0,parse_dates=[0])
qc_testing_data = testing_data.loc["Quebec"]

active_url = "https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/timeseries_prov/active_timeseries_prov.csv"
active_data = pd.read_csv(active_url,index_col=0,parse_dates=[0])
qc_active_data = active_data.loc["Quebec"]

# print(qc_cases_data)
# print(qc_mortality_data)
# print(qc_testing_data)
# print(qc_recovered_data)
# print(qc_active_data)


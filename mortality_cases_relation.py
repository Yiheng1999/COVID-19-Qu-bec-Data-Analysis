from read_data import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Normally it takes 7 days from diagnosis to decease. I shift the cases to right by 7 to match the mortality date.
# For example, the deaths of 08-03-2020 is corresponding to the diagnosis cases in 01-03-2020

qc_cases_data = qc_cases_data[36:len(qc_cases_data.index)-7]

date = qc_mortality_data["date_death_report"]
cases = qc_cases_data["cases"]
deaths = qc_mortality_data["deaths"]

fig, ax = plt.subplots()
ax.plot(date, deaths, color='r', label="Mortality per Day")
ax.plot(date, cases, color='b', label="Cases per Day")
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.xlabel("Mortality Date")

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_formatter(ticker.NullFormatter())

plt.title("COVID-19 New Mortality Per Day And New Cases Per Day")

plt.savefig("mortality.jpg")

plt.show()


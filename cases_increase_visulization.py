from read_data import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

date = qc_cases_data["date_report"]
cases = qc_cases_data["cases"]
cumulative_cases = qc_cases_data["cumulative_cases"]

plt.plot(date, cases, color='r', label="Cases Increased Each Day")
plt.plot(date, cumulative_cases, color='b', label="Cumulative Cases")
plt.legend(loc='upper left')

# my_x_ticks = np.arange(0, date.size, 5)
# plt.xticks(my_x_ticks)

# plt.xticks(np.arange(0,date.size+1, 10.0))
# plt.xticks(rotation=90)

fig, ax = plt.subplots()
ax.plot(date, cases, color='r', label="Cases Increased Each Day")
ax.plot(date, cumulative_cases, color='b', label="Cumulative Cases")
plt.legend(loc='upper left')
plt.xticks(rotation=45)

ax.xaxis.set_major_locator(mticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))
ax.xaxis.set_minor_formatter(mticker.NullFormatter())

plt.title("The COVID-19 Cases Increase Trend From January 25")

plt.savefig("cases.jpg")

plt.show()

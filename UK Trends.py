import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import pearsonr

cases = pd.read_csv('Articles/Images and Code/COVID 19 Data/NHS Data/data_2021-Jul-27-2.csv')
deaths = pd.read_csv('Articles/Images and Code/COVID 19 Data/NHS Data/data_2021-Jul-27-3.csv')
vaccinations = pd.read_csv('Articles/Images and Code/COVID 19 Data/NHS Data/data_2021-Jul-27.csv')

cases = cases.drop(cases.iloc[:, :3], axis = 1)
cases = cases.drop('cumCasesBySpecimenDate', axis = 1)
cases.iloc[:, 0] = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in cases.iloc[:, 0]]

deaths = deaths.drop(deaths.iloc[:, :3], axis = 1)
deaths = deaths.drop('cumDeaths28DaysByDeathDate', axis = 1)
deaths.iloc[:, 0] = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in deaths.iloc[:, 0]]

vaccinations = vaccinations.drop(vaccinations.iloc[:, :3], axis = 1)
vaccinations = vaccinations.drop('cumPeopleVaccinatedFirstDoseByPublishDate', axis = 1)
vaccinations.iloc[:, 0] = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in vaccinations.iloc[:, 0]]

cases_and_deaths = pd.merge(cases, deaths, on = 'date', how = 'inner')

df = pd.merge(cases_and_deaths, vaccinations, on = 'date', how = 'outer')

df.columns = ['Date', 'Cases', 'Deaths', 'Vaccinations']

df['Vaccinations'] = df['Vaccinations'].fillna(0)

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
plt.title('Cases and Deaths to Vaccinations in the UK')
ax.plot(df.iloc[:, 0], df.iloc[:, 1], label = 'Cases')
ax.plot(df.iloc[:, 0], df.iloc[:, 2], c = 'C2', label = 'Deaths')
ax.legend(loc = 2)
ax2.plot(df.iloc[:, 0], df.iloc[:, 3], c = 'C1', label = 'Vaccinations')
plt.xticks(rotation = 45)
ax2.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Cases and Deaths')
ax2.set_ylabel('Vaccinations')
plt.grid()
plt.savefig('Cases, Deaths and Vaccination', dpi = 500)
plt.show()

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
plt.title('Cases to Deaths in the UK')
ax.plot(df.iloc[:, 0], df.iloc[:, 1], label = 'Cases')
ax.legend(loc = 2)
ax2.plot(df.iloc[:, 0], df.iloc[:, 2], c = 'C2', label = 'Deaths')
ax2.legend(loc = 1)
plt.xticks(rotation = 45)
ax.set_xlabel('Date')
ax.set_ylabel('Cases')
ax2.set_ylabel('Deaths')
plt.grid()
plt.savefig('Cases and Deaths', dpi = 500)
plt.show()


df2 = pd.merge(cases_and_deaths, vaccinations, on = 'date', how = 'inner')
df2.columns = ['Date', 'Cases', 'Deaths', 'Vaccinations']
df2['Vaccinations'] = df2['Vaccinations'].fillna(0)

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
plt.title('Deaths to Vaccines in the UK')
ax.plot(df2.iloc[:, 0], df2.iloc[:, 2], label = 'Deaths')
ax.legend(loc = 2)
ax2.plot(df2.iloc[:, 0], df2.iloc[:, 3], c = 'C2', label = 'Vaccinations')
ax2.legend(loc = 1)
plt.xticks(rotation = 45)
ax.set_xlabel('Date')
ax2.set_ylabel('Vaccinations')
ax.set_ylabel('Deaths')
plt.grid()
plt.savefig('Deaths and Vaccines', dpi = 500)
plt.show()

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
plt.title('Cases to Vaccines in the UK')
ax.plot(df2.iloc[:, 0], df2.iloc[:, 1], label = 'Cases')
ax.legend(loc = 2)
ax2.plot(df2.iloc[:, 0], df2.iloc[:, 3], c = 'C2', label = 'Vaccinations')
ax2.legend(loc = 1)
plt.xticks(rotation = 45)
ax.set_xlabel('Date')
ax2.set_ylabel('Vaccinations')
ax.set_ylabel('Cases')
plt.grid()
plt.savefig('Cases and Vaccines', dpi = 500)
plt.show()


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit([df2.iloc[:, 1]], [df2.iloc[:, 2]])

predictions = regressor.predict([df2.iloc[:, 1]])
print(df2)

corr1, _ = pearsonr(df2.iloc[:, 1], df2.iloc[:, 2])
print('Pearsons correlation: %.3f' % corr1)

corr2, _ = pearsonr(df2.iloc[:, 2], df2.iloc[:, 3])
print('Pearsons correlation: %.3f' % corr2)

corr3, _ = pearsonr(df2.iloc[:, 1], df2.iloc[:, 3])
print('Pearsons correlation: %.3f' % corr3)

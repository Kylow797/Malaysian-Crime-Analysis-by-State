import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#The Crime
df = pd.read_csv('crime_district.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

kelantanDF = df[(df['state'] == 'Kelantan') & (df['year'] == 2023)]
selangorDF = df[(df['state'] == 'Selangor') & (df['year'] == 2023)]

kelantanTC = kelantanDF['crimes'].sum()
selangorTC = selangorDF['crimes'].sum()

print(kelantanTC, selangorTC)

#The Population
dfPop = pd.read_csv('population_state.csv')

dfPop['date'] = pd.to_datetime(dfPop['date'])
dfPop['year'] = dfPop['date'].dt.year

kelantanPop = 1000*dfPop.loc[(dfPop['state'] == 'Kelantan') & (dfPop['year'] == 2024) & (dfPop['ethnicity'] == 'overall')& (dfPop['age'] == 'overall')& (dfPop['sex'] == 'both'), 'population'].iloc[0]
selangorPop = 1000*dfPop.loc[(dfPop['state'] == 'Selangor') & (dfPop['year'] == 2024) & (dfPop['ethnicity'] == 'overall')& (dfPop['age'] == 'overall')& (dfPop['sex'] == 'both'), 'population'].iloc[0]

#print(kelantanPop)
#print(selangorPop)

kelCrimePerCapita = kelantanTC/kelantanPop *100000
selCrimePerCapita = selangorTC/selangorPop *100000

states = ['Kelantan', 'Selangor']
crimeRates = [kelCrimePerCapita, selCrimePerCapita]

plt.figure(figsize = (8, 5))
plt.bar(states, crimeRates, color = ['red','yellow'])

plt.title('Crime Rates per 100000 People by Malaysian State', fontsize = 15)
plt.xlabel('State', fontsize = 12)
plt.ylabel('Crime Rate per 100000 people', fontsize = 12)

plt.tight_layout()
plt.show()
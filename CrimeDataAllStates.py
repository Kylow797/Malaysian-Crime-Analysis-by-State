import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Crime Data
df = pd.read_csv('crime_district.csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Filter data for the year 2023
df_2023 = df[df['year'] == 2023]

# Calculate total crimes for each state in 2023
total_crimes_by_state = df_2023.groupby('state')['crimes'].sum().reset_index()

# Load the Population Data
dfPop = pd.read_csv('population_state.csv')
dfPop['date'] = pd.to_datetime(dfPop['date'])
dfPop['year'] = dfPop['date'].dt.year

# Filter population data for 2024, overall ethnicity, age, and sex
dfPop_2024 = dfPop[(dfPop['year'] == 2024) & 
                   (dfPop['ethnicity'] == 'overall') & 
                   (dfPop['age'] == 'overall') & 
                   (dfPop['sex'] == 'both')]

# Merge crime and population data
merged_df = pd.merge(total_crimes_by_state, dfPop_2024[['state', 'population']], on='state')

# Calculate crime rate per 100,000 people for each state
merged_df['crime_rate_per_100k'] = (merged_df['crimes'] / (merged_df['population'] * 1000)) * 100000

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(merged_df['state'], merged_df['crime_rate_per_100k'], color='lightblue')

plt.title('Crime Rates per 100,000 People by State (2023)', fontsize=15)
plt.xlabel('State', fontsize=12)
plt.ylabel('Crime Rate per 100,000 People', fontsize=12)
plt.xticks(rotation=90, ha='right')  # Rotate x labels for better readability
plt.tight_layout()
plt.show()

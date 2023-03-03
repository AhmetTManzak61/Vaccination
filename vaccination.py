import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

vacc_file_path = 'C:/Users/MONSTER/Desktop/country_vaccination_stats.csv'
vacc_data = pd.read_csv(vacc_file_path)
pd.options.display.max_columns = None

vacc_data['daily_vaccinations'] = vacc_data['daily_vaccinations'].fillna(vacc_data.groupby('country')['daily_vaccinations'].transform('min'))
#the line above replaces missing values with the minimum value

vacc_data = vacc_data.replace(np.nan,0)
#Replace NaN with 0 for the Kuwait case

df_by_country = vacc_data.groupby('country')
print(vacc_data.head(754))
#print to 754 so we can see Kuwait

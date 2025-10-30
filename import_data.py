
import pandas as pd
import matplotlib.pyplot as plt

path_data = '/Users/owenwyman/Data/ev228_data/'
fn_data = 'KRDU_temp_188708-202508.csv'


df_cos = pd.read_csv(path_data + fn_data)

print(df_cos)

max_temp = df_cos['metANN']

print(max_temp)
dates = df_cos['YEAR']

max_temp = max_temp[1:]
dates = dates[1:]

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(dates, max_temp)
ax.set_xlabel('Year')
ax.set_ylabel('Annual Mean Temperature (°C)')
ax.set_title('Annual Mean Temperature')
plt.show()

import pandas as pd


path_data = '/User/[owenwyman]/Data/ev228_data/'
fn_data = '/content/KRDU_temp_188708-202508.csv'


df_cos = pd.read_csv(fn_data)

print(df_cos)

max_temp = df_cos['maximumT']
dates = df_cos['Year_Month']

max_temp = max_temp[1:]
dates = dates[1:]

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(dates, max_temp)
ax.set_xlabel('Year')
ax.set_ylabel('Maximum Temperature (°F)')
ax.set_title('Monthly Maximum Temperature at KRDU')
plt.show()

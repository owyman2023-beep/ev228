import pandas as pd


path_data = '/User/[owenwyman]/Data/ev228_data/'
fn_data = '/content/KRDU_temp_188708-202508.csv'


df_cos = pd.read_csv(fn_data)

print(df_cos)



fig, ax = plt.subplots(figsize=(12,6))
ax.plot(dates, max_temp)
ax.set_xlabel('Year')
ax.set_ylabel('Maximum Temperature (°F)')
ax.set_title('Monthly Maximum Temperature in Colorado Springs')
plt.show()

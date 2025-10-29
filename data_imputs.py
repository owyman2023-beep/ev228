import fun_process_data as fpd
import matplotlib.pyplot as plt
import pandas as pd
output1, output2 = fpd.process_data('/Users/owenwyman/Data/ev228_data/practical4/USW00093009_temp_190801-202508.csv', 'metANN', 'YEAR')

df = pd.concat([output2, output1], axis=1)
print(df)
filtered_data = df[df['metANN'] != 999.90]
print(filtered_data)

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(filtered_data['YEAR'], filtered_data['metANN'])
ax.set_xlabel('Year')
ax.set_ylabel('Annual Mean Temperature (°C)')
ax.set_title('Annual Mean Temperature')
plt.show()
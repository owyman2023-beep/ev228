import fun_plots as fp
import fun_import as fi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

file_path = "/Users/owenwyman/Data/ev228_data/"
file_name = 'KRDU_temp_188708-202508.csv'
fig_path = '/Users/owenwyman/Data/ev228_data/figures/'
fig_name = '1_linregress.png'

var = 'metANN'
time_var = 'YEAR'

df, df_year = fi.import_ghcn(file_path=file_path + file_name, var=var)
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

result = stats.linregress(filter_year, filter_data)


slope = {result.slope}
yint = {result.intercept}
rvalue = {result.rvalue}
pvalue = {result.pvalue}
stderr = {result.stderr}

print(slope)

plt.scatter(filter_year, filter_data)
plt.plot(filter_year, yint + slope*filter_year, color="#2b63dc", linewidth=2.5)
plt.xlabel('Years')
plt.xlim(1948, 2025)
plt.ylabel('Mean Annual Temperature (deg C)')
plt.title('Mean Annual Temperature of Reigliegh DURHAM scat regress', size=8)
plt.savefig(fig_path + fig_name, dpi=400)


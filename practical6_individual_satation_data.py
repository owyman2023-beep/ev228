import fun_plots as fp
import fun_import as fi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = "/Users/owenwyman/Data/ev228_data/practical6/"
file_name = 'SGM00061600_temp_189201-202508.csv'
fig_path = '/Users/owenwyman/Data/ev228_data/figures/'
fig_name = '1_sgm.png'

var = 'metANN'
time_var = 'YEAR'

df, df_year = fi.import_ghcn(file_path=file_path + file_name, var=var)
filter_data = df[df != 999.9]
filter_year = df_year[df != 999.9]

# print(filter_data)
# print(df_year)

mean_var = np.mean(filter_data)
stdev_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var, stdev_var, max_var, min_var)

fp.timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)
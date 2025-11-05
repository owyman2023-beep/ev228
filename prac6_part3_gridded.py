import fun_plots as fp
import fun_import as fi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr

path = '/Users/owenwyman/Data/ev228_data/practical6/'
fn = 'era5_10mwind_1980-1989.nc'
out_path = '/Users/owenwyman/Data/ev228_data/figures/'
out_fn = '2_era6prac6.png'

da = fi.import_era5(file_path=path + fn, var='si10')
da_timemn = da.mean(dim='valid_time')
da_toplot = da_timemn - 15
fp.map(da_toplot, out_path=out_path, out_name=out_fn)



# mean_var = np.mean(filter_data)
# stdev_var = np.std(filter_data)
# max_var = np.max(filter_data)
# min_var = np.min(filter_data)
# print(mean_var, stdev_var, max_var, min_var)


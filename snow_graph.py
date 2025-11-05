import fun_plots as fp
import fun_import as fi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr

path = '/Users/owenwyman/Data/ev228_data/individual_project/'
fn = 'faf2d27731ed6827c0cb7c284be3f43b.nc'
out_path = '/Users/owenwyman/Data/ev228_data/figures/'
out_fn = '1_proj.png'



da = fi.import_era5(file_path=path + fn, var='csf')
da_timemn = da.mean(dim='valid_time')
# da_toplot = da_timemn 
fp.map(da_timemn, out_path=out_path, out_name=out_fn)



# mean_var = np.mean(da_timemn)
# stdev_var = np.std(da_timemn)
# max_var = np.max(da_timemn)
# min_var = np.min(da_timemn)
# print(mean_var, stdev_var, max_var, min_var)


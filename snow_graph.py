import fun_plots as fp
import fun_import as fi
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cf

path = '/Users/owenwyman/Data/ev228_data/individual_project/'
fn = 'edd98c954b619fc3f8c3ad46add9b76c.nc'
out_path = '/Users/owenwyman/Data/ev228_data/figures/'
out_fn = '4_proj.png'


da = fi.import_era5(file_path=path + fn, var='sde')



mu = da.mean(dim = 'valid_time')
sigma = da.std(dim = 'valid_time')
z_score = (da-mu) / sigma
da1 = z_score.sel(valid_time = '2024-02-01')

# da_timemn = da.mean(dim='valid_time')

projection = ccrs.PlateCarree()
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
da1.plot.pcolormesh(
    x = 'longitude',
    y = 'latitude',
    ax = ax,
    transform = ccrs.PlateCarree(),
    extend = 'both'
)
 
ax.add_feature(cf.STATES, linestyle=':')
ax.add_feature(cf.BORDERS, linestyle='--')

ax.set_extent([-109.3, -101.8, 36.8, 41.2], crs=ccrs.PlateCarree())
ax.set_title('Cumulative Snowfall in Colorado (1950-2025)')

plt.savefig(out_path + out_fn, dpi=300, bbox_inches='tight') 
plt.show()




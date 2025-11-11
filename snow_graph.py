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

#input desired year and month (between 1950-2025 / only january, febuary, or march / do not change day)
choose_time = '1984-03-01'


mu = da.mean(dim = 'valid_time')
sigma = da.std(dim = 'valid_time')
z_score = (da-mu) / sigma
da1 = z_score.sel(valid_time = choose_time)

# da_timemn = da.mean(dim='valid_time')
projection = ccrs.PlateCarree()
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
da1.plot.pcolormesh(
    x = 'longitude',
    y = 'latitude',
    ax = ax,
    transform = ccrs.PlateCarree(),
    extend = 'both',
    cbar_kwargs={'label': 'Z-score of Snow Depth (m)'}
)
 
ax.add_feature(cf.STATES, linestyle=':')
ax.add_feature(cf.BORDERS, linestyle='--')
ax.set_extent([-109.3, -101.8, 36.8, 41.2], crs=ccrs.PlateCarree())
ax.set_title('Colorado Snow Depth ' + choose_time)


mean_da1 = da1.mean()
# print (mean_da1.item())
print(f"Mean z-score for all Colorado data in {choose_time} is {mean_da1.item():.2f}")
if mean_da1 > .7:
    print("Historically signifigant above average snowfall in Colorado during " + choose_time)
elif mean_da1 > .4:
    print("Extremely high average snowfall in Colorado during " + choose_time)
elif mean_da1 > 0.22:
    print("Notably above average snowfall in Colorado during " + choose_time)
elif mean_da1 > 0:
    print("Above average snowfall in Colorado during " + choose_time)
elif mean_da1 > -0.22:
    print("Below average snowfall in Colorado during " + choose_time)
elif mean_da1 > -.4:
    print("Notably below average snowfall in Colorado during " + choose_time)
elif mean_da1 > -.7:
    print("Extremely high average snowfall in Colorado during " + choose_time)
else:  
    print("Historically signifigant below average snowfall in Colorado during " +choose_time)


plt.savefig(out_path + out_fn, dpi=300, bbox_inches='tight') 





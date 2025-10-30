import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import numpy as np

def plot_netcdf_variable(path_data, column):
    path_data = '/Users/owenwyman/Data/ev228_data/era5_t2m_1997-2025.nc'
    ds = xr.open_dataset(path_data)
    t2m_variable = ds[column]
    t2m_average = t2m_variable.mean('valid_time')
    t2m_average.plot()
    plt.title('Plot of 2-meter Temperature (t2m) from 1997-2025')
    plt.show()

# print (t2m_variable)
# t2m_stat = t2m_variable.std or .max or .sum ('valid_time')
# or can do individual time t2m_variable.isel (valid_time=0) will just give jan 1997 data






def calculate_descriptive_statistics(data, dimensions=None):
    stats = {}
    stats['mean'] = data.mean(dim=dimensions).item() if dimensions else data.mean().item()
    stats['median'] = data.median(dim=dimensions).item() if dimensions else data.median().item()
    stats['std_dev'] = data.std(dim=dimensions).item() if dimensions else data.std().item()
    stats['min'] = data.min(dim=dimensions).item() if dimensions else data.min().item()
    stats['max'] = data.max(dim=dimensions).item() if dimensions else data.max().item()
    return stats
    print(stats)

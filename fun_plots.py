import sys
from icecream import ic
import matplotlib.pyplot as plt
import numpy as np

def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color="#2b63dc", linewidth=2.5)
    plt.xlabel('Years')
    plt.xlim(1892, 2025)
    plt.ylabel('Mean Annual Temperature (deg C)')
    plt.title('Mean Annual Temperature of Sir Seewoosagur Ramgoolam International Airport 1892-2025', size=8)
    plt.savefig(out_path + out_name, dpi=400)

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('Cumulative Snowfall in Colorado from 1940-2024')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('in')
    plt.savefig(out_path + out_name, dpi=400)

def bar(in_df, in_x=None, out_path='', out_name=''):

    fig, ax = plt.subplots(figsize=(8,6))
    ax.bar(annual_mean.index, annual_mean.values, color='skyblue', edgecolor='darkblue', linewidth=2, width=0.8, label=stats_label)
    ax.set_ylim(bottom=5, top=8)
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Halibut Weight (kg)')
    ax.set_title('Pacific Halibut Weight from 2019-2024')
    ax.set_xticks(annual_mean.index)
    ax.legend(loc='best', title="Statistics (2019-2025)")
    plt.savefig(out_path + out_name, dpi=400)

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:31:26 2021

@author: Sarat
"""

import rioxarray as rio
import numpy as np
import xarray as xr
import pandas as pd
import geopandas as gpd
from shapely.geometry import mapping
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import matplotlib.pyplot as plt
#########################################
#%%!!!!!! Use this section only to downscale from hourly to daily !!!!##

# ds = xr.open_mfdataset('D:/Evap_IMDAA/*.nc') # change the folder accordingly
# #####  temporal downscaling considering daily mean from all hourly values ##
# ds_daily = ds.resample(time='1D').mean('time')
#%% Use this section to calculate total ET and conversion ###
# Loading daily data obtained earlier #
ds = xr.open_dataset('evap_daily.nc') # change the folder accordingly
## Tot ET = Soil Evap + Canopy EVap
ds_tot_et = ds.EVARSS_sfc+ds.EVARSS_sfc # Total Et in kg/m2/s
#####
### convert to mm/day ##
ds_tot_et = ds_tot_et*86400 # Tot ET in mm/day

#%%Use this section to extract the area masked nc file using shapefile ###
## Load the shapefile corresponding to each sub-basin ###
### By default I loaded the whole Kaveri basin ###
fname = 'sub_basins_shp_1to9/sub1.shp' # change the file accordingly
shape = gpd.read_file(fname, crs='epsg:4326')
########################
## mask the tot ET array using shapefile ###
ds_tot_et.rio.set_spatial_dims(x_dim='longitude',y_dim='latitude', inplace=True)
ds_tot_et.rio.write_crs("epsg:4326", inplace=True)
ds_et_mask=ds_tot_et.rio.clip(shape.geometry.apply(mapping), shape.crs, 
                       drop=False)
#######
#%% Converting the array to time-series ###
## using latitude weights for better areal averaging ###
weights = np.cos(np.deg2rad(ds_et_mask.latitude))
weights.name = 'weights'
ds_1d=ds_et_mask.weighted(weights)
ds_daily_wm = ds_1d.mean(('latitude','longitude'))
########
ds_daily_wm=ds_daily_wm.to_pandas()
####
ds_1d_wm = pd.Series(data=ds_daily_wm, name = 'ET (mm/day)')
####
## Saving as csv file ####
ds_1d_wm.to_csv('ET_Scripts/et_kaveri.csv')   # change folder accordingly
#%% Plotting using default matplotlib ###
ds_1d_wm.plot(color='blue', ylabel='mm/day', xlabel='Time', 
              title='ET in Selected basin')


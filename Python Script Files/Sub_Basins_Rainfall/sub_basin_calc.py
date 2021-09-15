# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:52:34 2021

@author: Sarat
"""

import rioxarray as rio
import numpy as np
import datetime as dt
import xarray as xr
import proplot as plot
import pandas as pd
import geopandas as gpd
from shapely.geometry import mapping
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import imdlib as imd
import statsmodels.api as sm
import matplotlib.dates as mdates
#################################
rf=xr.open_dataset('D:/IMD_data/rain_1951_2020.nc')
######################################################
fname = 'sub_basins_shp_1to9/sub1.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s1=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
##################################################

fname = 'sub_basins_shp_1to9/sub2.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s2=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
###############################################################
fname = 'sub_basins_shp_1to9/sub3.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s3=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
##############################################

fname = 'sub_basins_shp_1to9/sub4.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s4=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
####################################################
fname = 'sub_basins_shp_1to9/sub5.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s5=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'sub_basins_shp_1to9/sub6.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s6=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#####################################################
fname = 'D:/Walter/Geospatial_DB/sub7.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s7=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
######################################################
fname = 'sub_basins_shp_1to9/sub8.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s8=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
######################################################
fname = 'sub_basins_shp_1to9/sub9.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s9=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
###################################################
fname = 'sub_basins_shp_10to15/sub10.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s10=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#######################################################
fname = 'sub_basins_shp_10to15/sub11.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s11=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'sub_basins_shp_10to15/sub12.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s12=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname ='sub_basins_shp_10to15/sub13.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s13=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#########################################################
fname ='sub_basins_shp_10to15/sub14.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s14=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
############################################################
fname = 'sub_basins_shp_10to15/sub15.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s15=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
############################################################

########################################################

##########################################################
rf_s1_avg = rf_s1.rain.mean('lat').mean('lon')
rf_s2_avg = rf_s2.rain.mean('lat').mean('lon')

rf_s3_avg = rf_s3.rain.mean('lat').mean('lon')

rf_s4_avg = rf_s4.rain.mean('lat').mean('lon')

rf_s5_avg = rf_s5.rain.mean('lat').mean('lon')

rf_s6_avg = rf_s6.rain.mean('lat').mean('lon')

rf_s7_avg = rf_s7.rain.mean('lat').mean('lon')
rf_s8_avg = rf_s8.rain.mean('lat').mean('lon')

rf_s9_avg = rf_s9.rain.mean('lat').mean('lon')
rf_s10_avg = rf_s10.rain.mean('lat').mean('lon')

rf_s11_avg = rf_s11.rain.mean('lat').mean('lon')
rf_s12_avg = rf_s12.rain.mean('lat').mean('lon')

rf_s13_avg = rf_s13.rain.mean('lat').mean('lon')
rf_s14_avg = rf_s14.rain.mean('lat').mean('lon')
rf_s15_avg = rf_s15.rain.mean('lat').mean('lon')
##########################################################
rf_s1_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub1.csv')
rf_s2_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub2.csv')
rf_s3_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub3.csv')

rf_s4_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub4.csv')
rf_s5_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub5.csv')
rf_s6_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub6.csv')

rf_s7_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub7.csv')
rf_s8_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub8.csv')
rf_s9_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub9.csv')

rf_s10_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub10.csv')
rf_s11_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub11.csv')
rf_s12_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub12.csv')

rf_s13_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub13.csv')
rf_s14_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub14.csv')
rf_s15_avg.to_pandas().to_csv('Sub_Basins_Rainfall/sub15.csv')
#########################################################

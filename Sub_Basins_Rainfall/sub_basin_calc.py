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
fname = 'D:/Walter/Geospatial_DB/sub1.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s1=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
##################################################

fname = 'D:/Walter/Geospatial_DB/sub2.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s2=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
###############################################################
fname = 'D:/Walter/Geospatial_DB/Geospatial_DB/sub3.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s3=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
##############################################

fname = 'D:/Walter/Geospatial_DB/sub3.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s3=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
####################################################
fname = 'D:/Walter/Geospatial_DB/Geospatial_DB/sub4.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s4=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'D:/Walter/Geospatial_DB/sub4.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s4=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#####################################################
fname = 'D:/Walter/Geospatial_DB/sub5.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s5=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
######################################################
fname = 'D:/Walter/Geospatial_DB/sub6.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s6=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
######################################################
fname = 'D:/Walter/Geospatial_DB/sub7.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s7=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
###################################################
fname = 'D:/Walter/Geospatial_DB/sub8.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s8=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#######################################################
fname = 'D:/Walter/Geospatial_DB/sub9.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s9=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'D:/Walter/Geospatial_DB/sub10.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s10=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'D:/Walter/Geospatial_DB/sub11.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s11=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
#########################################################
fname = 'D:/Walter/Geospatial_DB/sub12.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s12=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
############################################################
fname = 'D:/Walter/Geospatial_DB/sub13.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s13=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
############################################################
fname = 'D:/Walter/Geospatial_DB/sub14.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s14=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
########################################################
fname = 'D:/Walter/Geospatial_DB/sub15.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s15=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
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
rf_s1_avg.to_pandas().to_csv('D:/Walter/sub1.csv')
rf_s2_avg.to_pandas().to_csv('D:/Walter/sub2.csv')
rf_s3_avg.to_pandas().to_csv('D:/Walter/sub3.csv')

rf_s4_avg.to_pandas().to_csv('D:/Walter/sub4.csv')
rf_s5_avg.to_pandas().to_csv('D:/Walter/sub5.csv')
rf_s6_avg.to_pandas().to_csv('D:/Walter/sub6.csv')

rf_s7_avg.to_pandas().to_csv('D:/Walter/sub7.csv')
rf_s8_avg.to_pandas().to_csv('D:/Walter/sub8.csv')
rf_s9_avg.to_pandas().to_csv('D:/Walter/sub9.csv')

rf_s10_avg.to_pandas().to_csv('D:/Walter/sub10.csv')
rf_s11_avg.to_pandas().to_csv('D:/Walter/sub11.csv')
rf_s12_avg.to_pandas().to_csv('D:/Walter/sub12.csv')

rf_s13_avg.to_pandas().to_csv('D:/Walter/sub13.csv')
rf_s14_avg.to_pandas().to_csv('D:/Walter/sub14.csv')
rf_s15_avg.to_pandas().to_csv('D:/Walter/sub15.csv')
#########################################################




















fname = 'D:/Walter/Geospatial_DB/Geospatial_DB/cauvery_subbasins.shp'
ind_shape = gpd.read_file(fname, crs='epsg:4326')
rf.rio.set_spatial_dims(x_dim='lon',y_dim='lat', inplace=True)
rf.rio.write_crs("epsg:4326", inplace=True)
rf_s4=rf.rio.clip(ind_shape.geometry.apply(mapping), ind_shape.crs, 
                       drop=False)
rf_s4.rain.isel(time=450).plot()
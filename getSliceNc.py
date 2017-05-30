import numpy as np
import cPickle as pickle
#import matplotlib.colors as mcolors
import xarray as xr
import sys,os

if len(sys.argv)==3:
    pre = sys.argv[1]
    iter = int(sys.argv[2])
else:
    sys.exit('USAGE: python getSliceNc.py pre iter')
    

#x slice
try:
    os.mkdir('../results/'+pre+'/_Model/input/slices')
except:
    pass

if 1:
    dss = xr.open_dataset('../results/'+pre+'/_Model/input/ds%010d.nc'%iter,
                      chunks={'YC':1,'YG':1})

    dss=dss.isel(YG=1,YC=1,time=0)
    print(dss)
    dss.to_netcdf('../results/'+pre+'/_Model/input/slices/'+pre+'SliceY220.nc',mode='w')
    dss.close()

    dss = xr.open_dataset('../results/'+pre+'/_Model/input/ds%010d.nc'%iter,
                              chunks={'Z':1,'Zl':1})

    dss=dss.isel(Z=230,Zl=230,time=0)
    print(dss)
    dss.to_netcdf('../results/'+pre+'/_Model/input/slices/'+pre+'SliceZ230.nc',mode='w')
    dss.close()

dss = xr.open_dataset('../results/'+pre+'/_Model/input/ds%010d.nc'%iter,
                          chunks={'Z':1,'Zl':1})
#dss = xr.open_dataset('/p/cwfs/jklymak/scr/LWRegrid4/'+pre+'/_Model/input/ds%010d.nc'%iter,
#                          chunks={'Z':1,'Zl':1})

dss=dss.isel(Z=300,Zl=300,time=0)
print(dss)
dss.to_netcdf('../results/'+pre+'/_Model/input/slices/'+pre+'SliceZ300.nc',mode='w')
dss.close()

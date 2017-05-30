import xarray as xr
import xmitgcm as xm
import numpy as np
import sys

pre = sys.argv[1]
iter=int(sys.argv[2])

iters = [iter]
print('%d'%iter)
ddir='../results/'+pre+'/_Model/input/'
print ddir
dss =[[],[],[]]

dss = xm.open_mdsdataset(ddir,iters=[iter,],
                                delta_t=20.,endian='<',geometry='cartesian',
                                prefix=['T','V','U','Eta','W','PH','PHL','KLeps','Conv','Ebt','Ebc','uPbc','uPbt','vPbt','vPbc'])
print(dss)
dss.to_netcdf(ddir+'ds%010d.nc'%iter)
dss.close()

# can open one, on transfer queue.  Can't open two.
# to_netcdf fails because it is forcing endianess and loads whole thing in.
# with chunking, no write?  1-level chunks.  No
#    30-level chunks?  No
#    100-level chunks?  No
# so chuninking doesn't seem to work.
# set ThreadPool(10) and printing works
# and saving works...
# chunking?  works.  Not sure that it helps
# can't read in 'W' as well...

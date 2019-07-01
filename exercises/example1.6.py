# Imports
import pylab as pl
import sciris as sc
import multiprocessing as mp

# Set parameters
xmin = 0
xmax = 10
npts = 200
std = 0.1
repeats = 100000
x = pl.linspace(xmin, xmax, npts)
run_series = True
run_manual = True
run_sciris = True
do_plot = True

# Define the random wave generator
def randgen(std):
    pl.seed(int(std*100))
    a = 0.2*pl.cos(x)*pl.sqrt(repeats)
    b = pl.zeros(npts)
    for r in range(repeats):
        b += (0.5-pl.rand(npts))*std
    return a+b

sdlk

# Set arguments for the parallel run
noisevals = pl.linspace(0,1,21)

# Run in series
if run_series:
    sc.tic()
    data = []
    for noiseval in noisevals:
        output = randgen(noiseval)
        data.append(output)
    sc.toc()

# Run in parallel -- manual way
if run_manual:
    sc.tic() 
    multipool = mp.Pool(processes=mp.cpu_count())
    data = multipool.map(randgen, noisevals)
    multipool.close()
    multipool.join()
    sc.toc()

# Run in parallel -- easy way
if run_sciris:
    sc.tic() 
    data = sc.parallelize(randgen, noisevals)
    sc.toc()

# Create 3D plot
if do_plot:
    sc.surf3d(pl.array(data))




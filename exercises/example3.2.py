import pylab as pl

# Simulation parameters
ncells = 1000
tmax = 500
dt = 1
period = 30

# Calculate spikes
pl.seed(1)
spikelist = []
tvec = pl.arange(0,tmax,dt)
firingrate = 5+4*pl.sin(tvec/period)
npts = len(tvec)
for t in range(npts):
    for c in range(ncells):
        if pl.rand() < firingrate[t]*dt/1000:
            spikelist.append([t,c])
spikedata = pl.array(spikelist)

# Average firing rate
averagerate = pl.zeros(npts)
for spike in spikedata:
    averagerate[spike[0]] += 1.0/ncells*1000

# Trend line
trendline = averagerate[:]
for repeat in range(5):
    trendline = pl.convolve(trendline, [0.25, 0.5, 0.25], 'same')

# Set up figure and options
pl.rc('font', family='serif', size=14)
pl.figure(figsize=(16,12))

# Plot the raster
pl.axes([0.1,0.35,0.8,0.6])
pl.scatter(spikedata[:,0], spikedata[:,1], s=100, alpha=0.3)
pl.xlim((0,tmax))
pl.gca().spines['top'].set_visible(False)
pl.gca().spines['right'].set_visible(False)
pl.gca().spines['bottom'].set_visible(False)
pl.xticks([])
pl.ylabel('Cell ID')

# Plot the average firing rate
pl.axes([0.1,0.05,0.8,0.25])
pl.plot(tvec, averagerate, color=(0.7,0.7,0.7), label='Instantaneous')
pl.plot(tvec, trendline, color=(0,0.4,1.0), lw=3, label='Averaged')
pl.plot(tvec, firingrate, '--', color=(0,0,0), lw=2, label='Generator')
pl.xlim((0,tmax))
pl.ylim((0,pl.ylim()[1]))
pl.gca().spines['top'].set_visible(False)
pl.gca().spines['right'].set_visible(False)
pl.xlabel('Time (ms)')
pl.ylabel('Average firing rate (Hz)')
pl.legend(loc=(0.85,0.93))

# Add panel labels
pl.axes([0,0,1,1])
pl.gca().axis('off')
pl.text(x=0.02, y=0.95, s='A', fontsize=35, fontfamily='sans-serif')
pl.text(x=0.02, y=0.3, s='B', fontsize=35, fontfamily='sans-serif')

# Save the figure
pl.savefig('ocnc-example.png', dpi=150)
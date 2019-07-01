# Created by Eugene M. Izhikevich, February 25, 2003
# Converted to Python by Cliff Kerr, June 24, 2019
# Excitatory neurons Inhibitory neurons

import pylab as pl

Ne = 800
Ni = 200
re = pl.rand(Ne)
ri = pl.rand(Ni)
a = pl.hstack([0.02*pl.ones(Ne), 0.02+0.08*ri])
b = pl.hstack([0.2*pl.ones(Ne), 0.25-0.05*ri])
c = pl.hstack([-65+15*re**2, -65*pl.ones(Ni)])
d = pl.hstack([8-6*re**2, 2*pl.ones(Ni)])
S = pl.hstack([0.5*pl.rand(Ne+Ni,Ne), -pl.rand(Ne+Ni,Ni)])

v = -65*pl.ones(Ne+Ni) # Initial values of v
u = b*v # Initial values of u
firings = pl.empty((2,0)) # spike timings
for t in range(1000): # simulation of 1000 ms
    I = pl.hstack([5*pl.randn(Ne), 2*pl.randn(Ni)]) # thalamic input
    fired = pl.find( v>= 30) # indices of spikes
    if len(fired):
        firings = pl.hstack([firings, pl.array([t+0*fired,fired])])
        v[fired] = c[fired]
        u[fired] = u[fired]+d[fired]
        I = I+S[:,fired].sum(axis=1)
    v = v+0.5*(0.04*v**2+5*v+140-u+I) # step 0.5 ms
    v = v+0.5*(0.04*v**2+5*v+140-u+I) # for numerical
    u = u+a*(b*v-u) # stability

pl.scatter(firings[0,:],firings[1,:])
pl.show()
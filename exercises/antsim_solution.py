import pylab as pl

class Antsim:
    ''' Simulation of ants randomly walking '''    
    
    def makeants(self, numants=50):
        ''' Initialize the ants '''
        self.numants = numants
        self.x = pl.zeros(numants)
        self.y = pl.zeros(numants)
    
    def plotants(self, timesteps=150, stepsize=0.03):
        ''' Plot the ants '''
        pl.figure()
        for t in range(timesteps):
            pl.clf()
            self.x += stepsize*pl.randn(self.numants)
            self.y += stepsize*pl.randn(self.numants)
            pl.scatter(self.x, self.y)
            pl.xlim((-1, 1))
            pl.ylim((-1, 1))
            pl.title('t = %i / %i' % (t+1, timesteps))
            pl.pause(1e-3)
            

# Run the simulation
sim = Antsim()
sim.makeants(numants=100)
sim.plotants()

import pylab as pl

class Antsim:
    ''' Simulation of ants randomly walking '''    
    
    def makeants(self, numants=50):
        ''' Initialize the ants '''
        self.numants = numants # Initialize the number of ants
        # Set up the x coordinate: an array of zeros of length numants
        # Set up the y coordinate the same way
    
    def plotants(self, timesteps=150, stepsize=0.03):
        ''' Plot the ants '''
        pl.figure()
        for t in range(timesteps):
            pl.clf()
            # Increment the x position of each ant by an amount stepsize*randn()
            # Increment the y position of each ant by an amount stepsize*randn()
            # Scatter x vs .y
            # Set the x limits to (-1,1)
            # Set the y limits to (-1,1)
            # Set the plot title to show the current step and the total number of timesteps
            pl.pause(1e-3)
            

# Run the simulation
sim = Antsim()
sim.makeants(numants=100)
sim.plotants()
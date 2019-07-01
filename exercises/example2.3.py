import sciris as sc
import pylab as pl

class Animal(sc.prettyobj):

    def __init__(self, name, mass, velocity):
        self.name = name
        self.mass = mass
        self.velocity = velocity

    def energy(self):
        return 0.5*self.mass*self.velocity**2

# Create animals
worm   = Animal(name='worm',   mass=0.002, velocity=0.01) # shorthand: Animal('worm', 0.002, 0.01)
pigeon = Animal(name='pigeon', mass=0.086, velocity=9.6)
cat    = Animal(name='cat',    mass=7.3,   velocity=4.4)
animals = [worm, pigeon, cat]

# Save and load animals
pl.save('animals.npy', animals) # file must end .npy (for numpy)
saved_animals = pl.load('animals.npy')

# Check it worked
print(saved_animals[0])
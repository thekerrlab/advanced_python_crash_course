# Functional approach

masses = {'worm':0.002, 'pigeon':0.086, 'cat':7.3} # in kg
velocities = {'worm':0.01, 'pigeon':9.6, 'cat':4.4} # in m/s

def energy(mass, velocity):
    return 0.5*mass*velocity**2

print('Maximum kinetic energy for:')
for animal in masses.keys():
    KE = energy(masses[animal], velocities[animal])
    print(f'{animal}: {KE}')
    

# Object-oriented
    
class Animal():
    
    def __init__(self, name, mass, velocity):
        self.name = name
        self.mass = mass
        self.velocity = velocity
        
    def energy(self):
        return 0.5*self.mass*self.velocity**2
    
    
worm   = Animal(name='worm',   mass=0.002, velocity=0.01)
pigeon = Animal(name='pigeon', mass=0.086, velocity=9.6)
cat    = Animal(name='cat',    mass=7.3,   velocity=4.4)

print('Maximum kinetic energy for:')
for animal in [worm, pigeon, cat]:
    print(f'{animal.name}: {animal.energy()}') 
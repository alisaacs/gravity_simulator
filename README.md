# gravity_simulator
Python 3 script to simulate movement of point like particles in a gravitational field.

The module contains functions that simulate a "universe" of point particles.  The particles are electrically neutral and obey Newtonian physics.  Particles start with an initial mass, position and velocity.  While the simulation is running the gravitational force on each particle is calculated and its motion updates accordingly.

Note that you must install the pygame module before you can run this script (https://www.pygame.org/wiki/GettingStarted).

All classes and functions are contained in the gravity_classes.py file.
The remaining files contain short programs that make use of these functions to simulate various scenarios.

## Simulation Details

The forces acting on each particle in the simulation are calculated at each time step.  This is then used to find the motion of the particle, which is then shown in the display.  If two particles come close enough to each other they may collide and form a single particle.  Momentum and mass are conserved in collisions.

The time step used in the simulation adjusts depending on the velocity of the particles.  This is done to ensure collisions are always detected.  The speed of the simulation may also vary according to the processing capabilities of the computer running the script.  Due to these factors, the speed of particles as seen on the display is not fully representative of the actual speed of the particles.

Note that the simulation does not use SI units.  When entering mass, position, velocity or time, each simulation unit is equal to:

Mass:     10^24 kg
Time:     10^7  s
Distance: 10^9  m
Speed:    10^2  m/s

For example, to enter a mass of 10^30 kg, you would enter a value of 10^6 into the simulation.

## Example simulations

two_body.py: Simulates a two body system.  One small mass is in a stable orbit around a heavy mass.

three_body.py: Simulates a three body sysem.  One small mass is in a stable orbit around two heavy masses.  The two heavy masses are orbiting a common centre of mass.

solar_system.py:  Simulates a solar system with four planets.  All four planets are in stable circular orbits around the Sun.

n_body.py:  Simulates (by default) a system with 200 randomly distributed particles.




## Creating a simulation

Examples of simulations can be seen in the scripts included in this repo.

To create a script, create a universe object.  When doing this you must define the dimensions of the universe in pixels:

new_universe = universe(x_dimension, y_dimension)

This would create a universe called new_universe.  In the examples that follow we will continue using this name, but it can be replaced with any name you like.

As an example:

two_body = universe(300,300)

will create a universe called two_body with dimensions of 300x300 pixels.

Each pixel nominally represents a distance of 10^9 m (1 million km).


Once a universe is created you need to add particles.  This can be done in two ways, randomly or manually.

To add particles randomly use the command: 
new_universe.fillUniverse(n)
where n is the number of particles to add.  This command adds n particles, each of which will have a random velocity, mass and position.  new_universe should be replaced by the name of your universe.

To add particles mannually use the command:
new_universe.addParticle(particle(vector(x_position, y_position),mass,vector(x_velocity, y_velocity)))

For example
two_body.addParticle(particle(vector(150,150),6e3,vector(-0.005,0)))
creates a particle with position (150,150), mass 6e3 and velocity (-0.005,0)

To run a simulation use the command:
new_universe.run_simulation(time)

where time is the total time to simulate.

You may also use:
new_universe.run_simulation(time, tracks="True")
This command will show the tracks of each particle in the display and can be useful for seeing orbits clearly.


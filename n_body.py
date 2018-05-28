from gravity_classes import particle, vector, universe

## Creates a simulation with n particles
## Warning, making n very high may make simulation run very slowly!
## Press Ctrl-C to exit simulation if running very slowly
## Or exit by closing the pygame window

n = 200    						#change this to change number of particles

n_body = universe(500,500)		#change to change dimensions of screen (in pixels)
n_body.fillUniverse(n)

n_body.run_simulation(350)		#change to increase length of simulation
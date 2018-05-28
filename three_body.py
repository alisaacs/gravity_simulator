from gravity_classes import particle, vector, universe

## Simulation of three bodies in a stable orbit.
## In this simulation two heavy bodies orbit around a common centre of mass
## A third lighter body orbits at a distance


three_body = universe(500,500)
three_body.addParticle(particle(vector(260,260),1e3,vector(5,-5)))
three_body.addParticle(particle(vector(240,240),1e3,vector(-5,5)))
three_body.addParticle(particle(vector(250,350),2,vector(7.75,0)))


three_body.run_simulation(350)
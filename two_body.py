from gravity_classes import particle, vector, universe

## Simulation of two bodies in a stable orbit configuration


two_body = universe(300,300)
two_body.addParticle(particle(vector(150,150),6e3,vector(-0.005,0)))
two_body.addParticle(particle(vector(150,200),1,vector(30,0)))


two_body.run_simulation(350)
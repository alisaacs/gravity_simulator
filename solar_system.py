from gravity_classes import particle, vector, universe
import math

## Simulation of four planets in circular orbits around a Sun
## The solar mass is 1000 times greater than that of the planets
## To ensure the overall momentum of the system is zero, the Sun has a slight negative velocity
## System is stable over short time peiods, but may not be stable over a very long simulation
## Instability may be introduced from graviational interactions between the planets

## In this simulation the orbit tracks are shown.  This can be added to any simulation
## by setting Tracks="True" in the run_simulation command.


solar_system = universe(800,800)
solar_mass = 6e6

planets_momentum = 5*(math.sqrt((solar_system.big_g*solar_mass)/50) + math.sqrt((solar_system.big_g*solar_mass)/150) + math.sqrt((solar_system.big_g*solar_mass)/250) + math.sqrt((solar_system.big_g*solar_mass)/350))

solar_system.addParticle(particle(vector(400,400),solar_mass,vector(-1*planets_momentum/solar_mass,0)))
solar_system.addParticle(particle(vector(400,450),5,vector(math.sqrt((solar_system.big_g*solar_mass)/50),0)))
solar_system.addParticle(particle(vector(400,550),5,vector(math.sqrt((solar_system.big_g*solar_mass)/150),0)))
solar_system.addParticle(particle(vector(400,650),5,vector(math.sqrt((solar_system.big_g*solar_mass)/250),0)))
solar_system.addParticle(particle(vector(400,750),5,vector(math.sqrt((solar_system.big_g*solar_mass)/350),0)))

solar_system.run_simulation(350, tracks="True")
import random, math, pygame, pygame.gfxdraw

## Units are non-SI!
## 1 Distance Unit = 10^9 m
## 1 Time Unit = 10^7 s
## 1 Mass Unit = 10^24 kg




class particle:
	# Creates the actual physical objects in the universe
	def __init__(self, position, mass, velocity):
		self.position = position
		self.mass = mass
		self.velocity = velocity

	def applyForce(self, force, time_step):
		#F = ma
		acceleration = force.scalarDivision(self.mass)
		self.velocity = self.velocity.add(acceleration.scalarMultiply(time_step))

	def move(self, time_step):
		self.position = self.position.add(self.velocity.scalarMultiply(time_step))

	def getVelocity(self):
		return self.velocity

	def getMomentum(self):
		return self.velocity.scalarMultiply(self.mass)



class vector:
	# Useful to define (2D) vectors and associated functions
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def add(self,other):
		return vector(self.x + other.x, self.y + other.y)

	def subtract(self,other):
		return vector(self.x - other.x, self.y - other.y)

	def dotProduct(self,other):
		return self.x*other.x + self.y*other.y

	def scalarDivision(self, scalar):
		return vector(self.x/scalar, self.y/scalar)

	def scalarMultiply(self, scalar):
		return vector(self.x*scalar, self.y*scalar)

	def magnitude(self):
		return math.sqrt(self.dotProduct(self))

	def str(self):
		return str(self.x) + ', ' + str(self.y)
	


class universe:
	# Creates the space which particles can exist in
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.big_g = 6.67		# using non-SI units...
		self.particles = []
		self.time = 0

	def addParticle(self, particle):
		#Adds a specified particle to the universe
		self.particles.append(particle)

	def fillUniverse(self, n):
		#Adds n random particles to the universe
		for i in range(n):
			position = vector(self.x*random.random(),self.y*random.random())
			velocity = vector(10*(random.random()-0.5),10*(random.random()-0.5))
			mass = 1e3 * random.random()
			self.addParticle(particle(position, mass, velocity))

	def findTimeStep(self):
		max_speed = 1
		for particle in self.particles:
			if particle.getVelocity().magnitude() > max_speed:
				max_speed = particle.getVelocity().magnitude()
		return 1/max_speed

	def forceGravity(self, a, b):
		#Calculates gravitational force applied on body a by body b
		r = (a.position.subtract(b.position)).magnitude()
		unit_vector = (a.position.subtract(b.position)).scalarDivision(r)   
		return unit_vector.scalarMultiply((-1*self.big_g*a.mass*b.mass)/(math.pow(r,2)))

	def totalForce(self, a):
		#Calculates total gravitational force applied on a body
		total_force = vector(0,0)
		for particle in self.particles:
			if particle == a:
				pass
			else:
				total_force = total_force.add(self.forceGravity(a, particle))
		return total_force

	def collisions(self):
		#Look for collisions and act when found
		collision_radius = 2				

		for i in self.particles:
			for j in self.particles:
				if i == j:
					pass
				else:
					r = (i.position.subtract(j.position)).magnitude()
					if r < collision_radius:
						#Particles collided!
						if (i in self.particles) and (j in self.particles):
							momentum = (i.getMomentum()).add(j.getMomentum())
							mass = i.mass + j.mass
							position = (i.position.add(j.position)).scalarDivision(2)
							velocity = momentum.scalarDivision(mass)
							self.addParticle(particle(position, mass, velocity))
							self.particles.remove(i)
							self.particles.remove(j)

	def checkPositions(self):
		#Checks particle is still in universe and deletes particle if it escaped
		for i in self.particles:
			if i.position.x > self.x:
				self.particles.remove(i)
			elif i.position.y > self.y:
				self.particles.remove(i)
			elif i.position.x < 0:
				self.particles.remove(i)
			elif i.position.y < 0:
				self.particles.remove(i)

	def update(self):
		#Calculate what happens when time passes
		time_step = self.findTimeStep()
		forces = []
		for particle in self.particles:
			forces.append((particle, self.totalForce(particle)))
		for particle,force in forces:
			particle.applyForce(force, time_step)		
			particle.move(time_step)
		self.collisions()
		self.checkPositions()
		self.time += time_step

	def create_display(self):
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)

		self.size = (self.x, self.y)
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()
		self.pygame_done = False

	def run_simulation(self, max_time, tracks = False):
		self.create_display()
		while not self.pygame_done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.pygame_done = True

			if tracks == False:
				self.screen.fill(self.BLACK)	
				
			for particle in self.particles:
				try:
					pygame.gfxdraw.pixel(self.screen, 
										int(particle.position.x), 
										int(particle.position.y),
										self.WHITE)
				except:
					print('Unable to draw particle at: ' + particle.position.str())

			pygame.display.flip()
			print(self.time)
			if self.time < max_time:
				self.update()

			self.clock.tick(60)
		pygame.quit()
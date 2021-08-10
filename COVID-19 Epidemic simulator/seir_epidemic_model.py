import particles
import simulator
import csv
import pickle
import matplotlib.pyplot as plt
import os
import numpy as np


path = ("plots")
CHECK_FOLDER = os.path.isdir(path)

# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.makedirs(path)
    
# frequency of plotting the epidemic states and saving images
plot_freq = 1000

# the object of class simulator contains .....
sim = simulator.Simulator(0,20)   

# the object of class Particles contains ...
particles = particles.Particles(sim) 

for i in range(sim.number_of_iter):
    if i%10==0:
        print("Completed {}/{} iterations".format(i, sim.number_of_iter ))
    
    # update the records on each epidemic state 
    particles.update_states(i, sim)
    
    # update the velocities and coordinates of particles
    particles.update_velocities(i, sim)
    particles.update_coordinates(sim)
    
    # increment the duration present at the current state for each particle
    particles.time_cur_state = particles.time_cur_state + sim.delta_t  # Increment the state time
    
    # get indexes of contagious particles (exposed, infected and severely infected states)
    # and return the indexes of the susceptible particles close to contagious ones within the disease transmittion distance
    new_cases = particles.get_new_cases_ids(i, sim)


    sim.susceptible_to_exposed(particles, new_cases)

    sim.exposed_to_infected(particles)
    
    sim.infected_to_recovered(particles)
  
    sim.infected_to_severe_infected(particles, i)
   
    sim.severe_infected_to_dead_recovered(particles, i)

    
    #plot the epidemic states
    if i>=plot_freq and i%plot_freq==0:
        plot = particles.plot(sim, i)



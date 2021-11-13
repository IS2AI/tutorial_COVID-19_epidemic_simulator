import pandas as pd
import numpy as np
from sklearn.neighbors import KDTree
import matplotlib.pyplot as plt
import random
import simulator
import pickle

class Particles():
    def __init__(self, simulator):
        """
        An object of class Particles is characterized by five parameters: 
            x (array): position coordinates on a 2D map for each particle in the array
            v (array): velocities of the particles in the array
            ages (array): an age distribution array of the particles
            time_cur_states (array): the total time present at the current state for each particle
            epidemic_state (array): the epidemic state of each particle in the array is encoded as:
            0: Susceptible, 1: Exposed, 2: Infected,
            3: Recovered Immunized, 4: Dead, 7: Severely Infected
        """
        
        
        # Randomly initializing the position coordinates. 
        # Offset by 0.5 to provide smooth distribution.
        np.random.seed(simulator.SEED+0*simulator.number_of_iter)
        self.x =  2*(np.random.random((simulator.NUMBER_OF_PARTICLES, 2))-0.5)
        
        # Randomly initialization of the particle velocities.         
        # Offset by 0.5 to provide smooth distribution.
        np.random.seed(simulator.SEED+1*simulator.number_of_iter)
        self.v =  2*(np.random.random((simulator.NUMBER_OF_PARTICLES, 2))-0.5)
        
        # Initialize the age distribution based on the age groups and age pyramid defined in the class Simulator
        self.ages = [ind*[age_order] for ind,age_order in zip(simulator.AGE_DISTRS, simulator.AGE_GROUPS)]
        self.ages = np.array([int(item) for sublist in self.ages for item in sublist])
        np.random.seed(simulator.SEED+2*simulator.number_of_iter)
        np.random.shuffle(self.ages)
        
        # Initialize the time array for all particles
        self.time_cur_state = np.zeros((simulator.NUMBER_OF_PARTICLES, 1)) 
        
        # Initialize the epidemic state of the particles
        self.epidemic_state = np.zeros((simulator.NUMBER_OF_PARTICLES,1),dtype=np.int8)   
        
        # Randomly initilalize particles to be at the  exposed state to start the epidemic
        np.random.seed(simulator.SEED+3*simulator.number_of_iter)
        np.put(self.epidemic_state,np.random.choice(range(simulator.NUMBER_OF_PARTICLES*1), simulator.INITIAL_EXPOSED, replace=False),1)
        
        # The dictionary and dataframe are used to store the information of each epidemic state at every iteration
        self.states= {}
        self.df = pd.DataFrame(columns=["ind", "days", "exposed", "infected", "severe infected", "recovered", "dead", "susceptible", "total cases"])

    
    def update_records(self, i, simulator):
        """The class method updates the dictionary of epidemic states 
        and stores these results with the provided iteration in the dataframe.
        Susceptible = 0; Exposed = 1; Infected = 2; Severe Infected = 7; Recovered = 3;
        Dead = 4.
        
        Parameters
        ----------
        i (int): An iteration number
        simulator (class object): An object of class Simulator that contains 
        simulation parameters (e.g. delta_t)
        Returns
        -------
        None.
        """

        self.states = {'exposed': np.where(np.copy(self.epidemic_state)==1, self.epidemic_state, 0), 
                       'infected': np.where(np.copy(self.epidemic_state)==2, self.epidemic_state, 0),
                       'recovered': np.where(np.copy(self.epidemic_state)==3, self.epidemic_state, 0),
                       'dead': np.where(np.copy(self.epidemic_state)==4, self.epidemic_state, 0),
                       'severe_inf':np.where(np.copy(self.epidemic_state)==7, self.epidemic_state, 0),
                       'susceptible':(simulator.NUMBER_OF_PARTICLES - np.count_nonzero(np.copy(self.epidemic_state))),
                       'total_cases':np.count_nonzero(np.copy(self.epidemic_state))
                           }
        

        self.df.loc[i,:] = [i, i*simulator.delta_t, np.count_nonzero(self.states['exposed']), np.count_nonzero(self.states['infected']),
                 np.count_nonzero(self.states['severe_inf']), np.count_nonzero(self.states['recovered']),
                 np.count_nonzero(self.states['dead']), self.states['susceptible'], self.states['total_cases']]

    def plot(self, simulator,i):
        """The plot function visualizes the epidemic dynamic curves for each state
        Parameters
        ----------
        simulator (class object): An object of class Simulator that contains 
        simulation parameters (e.g. NUMBER_OF_PARTICLES)
        Returns
        -------
        A plot figure
        """
        
        """
        Task 2: 
        Write a function of Class Particles called plot that visualizes the epidemic curves
        for each state. 
        The function takes two parameters:
        1) simulator, an object of class Simulator;
        2) i, the id number of the current iteration.
    
        The id should be featured in the title of the plot. 
        The function should save the plot in .png format in the plots subdirectory 
        under the name states_i.png, where i is the id number. 
        """
        # WRITE YOUR CODE HERE

        
        
    def update_velocities(self, i, simulator): # Particle class method
        """The class method updates velocities of particles. If a velocity for a particle exceeds
        the magnitude of self.INIT_V_MAX, it set to zero. The velocity for dead and severely
        infected particles is also set zero.
        
        Parameters
        -------
        i (int): An iteration number 
        simulator (class object): An object of class Simulator that contains simulation parameters 
        
        Returns
        -------
        None
         
        """
        if i%simulator.KDT_FREQ==0 | i%simulator.KDT_FREQ==1:
            np.random.seed(simulator.SEED+4*simulator.number_of_iter)
            self.v = self.v + simulator.speed_gain*(np.random.random((simulator.NUMBER_OF_PARTICLES, 2))-0.5)
            self.v = np.where((self.epidemic_state==4) | (self.epidemic_state==7), 0, self.v)
            self.v = np.where(abs(self.v)>simulator.INIT_V_MAX, 0, self.v)
    

    def update_coordinates(self, simulator):  
        """The function to update the coordinates of the particles at each iteration.
        The particles stay inside of the 2D boundaries, set to [-1,1] for both dimensions. 
        If a particle reaches one of the borders, it is sent to the opposite side. 
        For example, if x > 1, then update to x = -1.
        
        Parameters:
        simulator (class object): An object of class Simulator that contains simulation parameters 
         
        Returns
        -------
        None
        """
        
        """
        Task 1: 
        Write a function of Class Particles called update_coordinates. 
        The function takes simulator, an object of Class Simulator. 
        At each iteration update the coordinate by the distance moved at the current iteration. 
        (Hint: simulator.delta_t is the time a particle spends in each iteration.)
        Note, the particles must stay inside of the 2D boundaries, set to [-1,1] for both dimensions.
        If a particle reaches one of the borders, it should be sent to the opposite side. 
        For example, if x > 1, then update to x = -1.
        """
        # WRITE YOUR CODE HERE
        

        
    def get_new_cases_ids(self, i, simulator):
        """This function randomly selects a proportion of indexes representing contagious 
        particles (exposed, infected, severe infected) based on their disease
        transmittion rates.
        
        Parameters
        -------
        i (int): a number of the current iteration
        simulator (class object): An object of class Simulator that contains simulation parameters 
         
        Returns
        -------
        new_cases (list): list of particles that spread infection
         
        """
        exposed_id = np.array(np.nonzero(self.states['exposed'])[0])
        np.random.seed(simulator.SEED+5*simulator.number_of_iter+i)
        ind_end_exp = np.random.choice(len(exposed_id), int(np.ceil(simulator.TRANSMISSION_RATE_EXPOSED*len(exposed_id))), replace=False)
            
        infected_id = np.array(np.nonzero(self.states['infected'])[0])
    
        sev_infected_id = np.array(np.nonzero(self.states['severe_inf'])[0])
        np.random.seed(simulator.SEED+6*simulator.number_of_iter+i)
        ind_end_sev = np.random.choice(len(sev_infected_id), int(np.floor(simulator.TRANSMISSION_RATE_SEVERE_INFECT*len(sev_infected_id))), replace=False)
        
        array = np.hstack((exposed_id[ind_end_exp], infected_id, sev_infected_id[ind_end_sev])).ravel()
    
        contact_ids = [int(i) for sublist in KDTree(self.x, leaf_size=2, metric="manhattan").query_radius(self.x[array], 
                        r=simulator.init_cont_threshold)  for i in sublist]
        contact = KDTree(self.x, leaf_size=2, metric="manhattan").query_radius(self.x[array], 
                        r=simulator.init_cont_threshold)

        new_cases = [contact_ids[x] for x 
                              in (np.where(self.epidemic_state[contact_ids]==0))[0]]

        return new_cases
    
if __name__ == "__main__":

    # Create object of Classes Simulator and Particles
    simulator = simulator.Simulator()
    particles = Particles(simulator)
    
    particles.update_states(1, simulator)
    

    # Test ids: 1, 15, 37, 110, 201
    
    # Case 1: particles velocity and coordinates update at iteration 1.
    particles.update_velocities(1, simulator)
    v_test_1 = particles.v
    particles.update_coordinates(simulator) 
    x_test_1 = particles.x
    
    # Case 1: particles velocity and coordinates update at iteration 15.
    particles.update_velocities(15, simulator)
    v_test_2 = particles.v
    particles.update_coordinates(simulator) 
    x_test_2 = particles.x
    
    # Case 1: particles velocity and coordinates update at iteration 37.
    particles.update_velocities(37, simulator)
    v_test_3 = particles.v
    particles.update_coordinates(simulator) 
    x_test_3 = particles.x
    
    # Case 1: particles velocity and coordinates update at iteration 110.
    particles.update_velocities(110, simulator)
    v_test_4 = particles.v
    particles.update_coordinates(simulator)
    x_test_4 = particles.x
    
    # Case 1: particles velocity and coordinates update at iteration 201.
    particles.update_velocities(201, simulator)
    v_test_5 = particles.x
    particles.update_coordinates(simulator) 
    x_test_5 = particles.x

    # Load file for particles velocities and positions update check. 
    filename = 'metadata/particles_v_and_x.p'
    with open(filename, 'rb') as filehandler:
        reloaded_tuple = pickle.load(filehandler)

    
    # Test 1 for velocities and positions update.
    check_v_1 = np.setdiff1d(v_test_1, reloaded_tuple[0])
    check_x_1 = np.setdiff1d(x_test_1, reloaded_tuple[5])
    if check_v_1.size==0 and check_x_1.size==0:
        print("Successfully passed velocities and positions update Test 1.")
    else: 
        print("Error in velocities and positions update Test 1.")
        
    # Test 2 for velocities and positions update.
    check_v_2 = np.setdiff1d(v_test_2, reloaded_tuple[1])
    check_x_2 = np.setdiff1d(x_test_2, reloaded_tuple[6])
    if check_v_2.size==0 and check_x_2.size==0:
        print("Successfully passed velocities and positions update Test 2.")
    else: 
        print("Error in velocities and positions update Test 2.")
        
    # Test 3 for velocities and positions update.
    check_v_3 = np.setdiff1d(v_test_3, reloaded_tuple[2])
    check_x_3 = np.setdiff1d(x_test_3, reloaded_tuple[7])
    if check_v_3.size==0 and check_x_3.size==0:
        print("Successfully passed velocities and positions update Test 3.")
    else: 
        print("Error in velocities and positions update Test 3.")
        
    # Test 4 for velocities and positions update.
    check_v_4 = np.setdiff1d(v_test_4, reloaded_tuple[3])
    check_x_4 = np.setdiff1d(x_test_4, reloaded_tuple[8])
    if check_v_4.size==0 and check_x_4.size==0:
        print("Successfully passed velocities and positions update Test 4.")
    else: 
        print("Error in velocities and positions update Test 4.")
        
    # Test 5 for velocities and positions update.
    check_v_5 = np.setdiff1d(v_test_5, reloaded_tuple[4])
    check_x_5 = np.setdiff1d(x_test_5, reloaded_tuple[9])
    if check_v_5.size==0 and check_x_5.size==0:
        print("Successfully passed velocities and positions update Test 5.")
    else: 
        print("Error in velocities and positions update Test 5.")
        

    # Load dataframe with saved simulation results to check the plot function.
    particles.df = pd.read_pickle("metadata/data_for_plots.p")
    particles.plot(simulator, 25000)
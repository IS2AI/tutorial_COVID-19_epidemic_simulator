import numpy as np
import math
import particles
import pickle


class Simulator(): 
    def __init__(self, seed=0, num=20):
        '''
        The Simulator object contains model parameters for the epidemic 
        
        simulation of the population of interest. Particles move in a 2D
        
        map represented by a square with x limits (-1, 1) and y limits (-1, 1).
        '''
        self.SEED = seed
        self.NUMBER_OF_PARTICLES = 10000 
        self.INITIAL_EXPOSED = 10
        self.AGE_GROUPS = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.AGE_DISTRS = [1000,1000,1000,1000,1000,1000,1500,1000,1500]
        
        self.SIMULATION_LENGTH = num
        self.INIT_V_MAX = 0.5
        self.KT = 20
        self.KA = 10
        self.KDT_FREQ = 10
        self.T_INF = 5
        self.T_EXP = 2
        self.MORTALITY_RATE = 0.14
        self.TRANSMISSION_RATE_EXPOSED = 0.7
        self.TRANSMISSION_RATE_SEVERE_INFECT = 0.3
        self.Betta_age = [0, 0.0001, 0.0003, 0.0008, 0.0015, 0.006, 0.022, 0.051, 0.093]
        self.Betta = 0.093
       
        self.mean_dst = 1/math.sqrt(self.NUMBER_OF_PARTICLES)
        self.init_cont_threshold = 0.8*self.mean_dst/self.KT
        self.speed_gain = self.INIT_V_MAX/self.KA
        self.delta_t = self.init_cont_threshold/self.INIT_V_MAX
        self.number_of_iter = math.ceil(self.SIMULATION_LENGTH/self.delta_t)
        

    def susceptible_to_exposed(self, model, susceptible_contacted): 
        """class method to transition epidemic status of the particles from 
        susceptible to exposed. 
        
        Parameters:
        model: an object of the Class Particles
        susceptible_contacted (list): list of susceptible particles that were 
        close to contagious particles (exposed, infected, severe infected)
        in this iteration.
         
        """
        
        """
        Task 3: 
        Write a function of Class Simulator called susceptible_to_exposed that
        updates the epidemic status of particles from susceptible to exposed. 
        The function takes two parameters: 
        1) model, an object of Class Particles; 
        2) susceptible_contacted, a list of indices of susceptible particles 
        that were close to contagious particles (exposed, infected, severe infected)
        at the current iteration. 
        
        Using these indices the function should: 
        1) update the corresponding elements in the model.epidemic_state array to the exposed state;
        2) reset the corresponding elements in the model.time_cur_state array to 0. 
        """
        # WRITE YOUR CODE HERE


        
    def exposed_to_infected(self, model): 
        """class method to transition epidemic status of the particles from 
        exposed to infected after period of exposure (self.T_EXP). 
        
        Parameters:
        model: an object of the Class Particles
    
        """
        to_inf =np.where(((model.epidemic_state==1) & (model.time_cur_state >= self.T_EXP)), 
                   1, 0)
        
        model.epidemic_state = np.where(to_inf==1, 2, model.epidemic_state)
        model.time_cur_state = np.where(to_inf==1, 0, model.time_cur_state)  
        
        
    def infected_to_recovered(self, model):
        """class method to transition epidemic status of the particles from 
        infected to recovered state after infecttion period (self.T_INF). 
        
        Parameters:
        model: an object of the Class Particles
        
        """
        
        """
        Task 4: 
        Write a function of Class Simulator called infected_to_recovered following 
        the example code provided for the exposed_to_infected method. 
        The function takes model, an object of Class Particles. 
        The function should: 
        1) get the indices of the particles whose time at the current state 
        have reached T_INF in model.time_cur_state array; 
        2) for these indices update the model.epidemic_state to recovered and
        model.time_cur_state to 0.
        """
        # WRITE YOUR CODE HERE



    def infected_to_severe_infected(self, model, i): 
        """class method to transition epidemic status of the particles from 
        infected to severe infected state based on the age group. Based on the 
        SIR parameter for each age group certain number of particles is selected.
        
        Parameters:
        model: an object of the Class Particles
        i (int): the number of the current iteration
         
        """
        # This is the case of the same Betta across all age groups. Please comment
        #this section and uncomment the commented section below to use different 
        # parameter for transitioning different age groups
        sir_ind = np.where((model.epidemic_state==2))
        ser_ind = sir_ind[0]
        np.random.seed(self.SEED+7*self.number_of_iter+i)
        temp_ar = np.random.random((len(sir_ind[0]), 1))

        model.epidemic_state[ser_ind[np.where(temp_ar<(self.Betta*self.delta_t))[0]]] = 7
        
# =============================================================================
#         for i in self.AGE_GROUPS:
#             
#             ind_arr1 = np.where((model.epidemic_state==2)&(model.ages==i))[0]
#             np.random.seed(self.SEED+7*self.number_of_iter+i)
#             if (ind_arr1.size>0):
#                  temp_ar = np.random.random((ind_arr1.size, 1)) 
#                  model.epidemic_state[ind_arr1[temp_ar<(self.Betta_age[i-1]*self.delta_t)]] = 7
# =============================================================================


    def severe_infected_to_dead_recovered(self, model, i):
        """class method to transition epidemic status of the particles from 
        severe infected to dead or recovered. The function updates the 
        model.epidemic_state array for particles reached T_INF in the model.time_cur_state
        array
        
        Parameters:
        model: an object of the Class Particles
        i (int): the number of the current iteration
         
        """

        np.random.seed(self.SEED+8*self.number_of_iter+i)
        temp = np.random.random((self.NUMBER_OF_PARTICLES,1))
        
        ind_end_severe_inf = np.where((model.time_cur_state >= self.T_INF) & (model.epidemic_state == 7) & (temp>self.MORTALITY_RATE))
        model.epidemic_state[ind_end_severe_inf] = 3 
        ind_severe_inf = np.where((model.time_cur_state >= self.T_INF) & (model.epidemic_state == 7) & (temp<self.MORTALITY_RATE))
        model.epidemic_state[ind_severe_inf] = 4
    

    
            
if __name__ == "__main__":
    # Create object of classes Simulator and Particles
    simulator = Simulator()
    particles = particles.Particles(simulator)
    
    # Load file with the saved simulation results
    saved_sim = 'metadata/saved_simulation_results.p'
    with open(saved_sim, 'rb') as filehandler:
        tuple_elements = pickle.load(filehandler)
        
    # retrive the new cases ids
    susceptible_contacted = tuple_elements[0]
    # retrive the epidemic state arrays
    particles.epidemic_state = tuple_elements[2]
    # retrive the time at currect epidemic state for each particle
    particles.time_cur_state = tuple_elements[3]
   
    # Susceptible to exposed transition 
    simulator.susceptible_to_exposed(particles, susceptible_contacted)
    state_transition1 = particles.epidemic_state
    time_transition1 = particles.time_cur_state


    saved_sim = 'metadata/saved_simulation_results.p'
    with open(saved_sim, 'rb') as filehandler:
        tuple_elements = pickle.load(filehandler)
        

    # retrive the epidemic state arrays
    particles.epidemic_state = tuple_elements[2]
    # retrive the time at currect epidemic state for each particle
    particles.time_cur_state = tuple_elements[3]
    indices_1 = [1,2,3,4]
    particles.epidemic_state[indices_1]=2
    particles.time_cur_state[indices_1]=simulator.T_INF

    # Infected to recovered transition
    simulator.infected_to_recovered(particles)
    state_transition2 = particles.epidemic_state


        
    # Load file for transition checks 
    transition = 'metadata/transitions.p'
    with open(transition, 'rb') as filehandler:
        reloaded_tuple = pickle.load(filehandler)
        
    check_1 = np.subtract(state_transition1, reloaded_tuple[0])
    if np.count_nonzero(check_1)==0:
        print("1. Successfully passed susceptible to exposed status transition check.")
    else: 
        print("1. Error in susceptible to exposed status transition check.")
        
    check_2 = np.subtract(time_transition1, reloaded_tuple[1])
    if np.count_nonzero(check_2)==0:
        print("2. Successfully passed susceptible to exposed time resetting check.")
    else: 
        print("2. Error in susceptible to exposed time resetting check.")
        
    check_3 = np.subtract(state_transition2, reloaded_tuple[2])
    if np.count_nonzero(check_3)==0:
        print("3. Successfully passed infected to recovered status transition check.")
    else: 
        print("3. Error in infected to recovered status transition check.")
    


    
    
            


            
# ISSAI-AUA-Summer-School

## The particle-based SEIR (Susceptible-Exposed-Infected-Recovered) model.
 
 
<img width="626" alt="Particle" src="https://user-images.githubusercontent.com/57977216/129843469-d514ecfe-a637-414e-af0a-ca6f8d6fab42.PNG">

## Statechart of the particle-based SEIR simulator

There are seven states (encoded by a number): susceptible, exposed, infected, severe infected, recovered and dead. 

<img width="605" alt="SEIR" src="https://user-images.githubusercontent.com/57977216/129844735-565a278d-4f62-47ae-85df-b585597f5afe.PNG">


## Requirements:

1. Anaconda3 (with Jupyter included):
 https://docs.anaconda.com/anaconda/install/
2. Spyder IDE:
 https://www.spyder-ide.org
List of packages used in our sessions:
1. Numpy
2. Pandas
3. Scikit-learn
4. Random
5. Matplotlib
7. Math


## How to use? 

The simulator model contains three python files:

<img width="661" alt="Files" src="https://user-images.githubusercontent.com/57977216/129843685-8f8b9a38-5e66-4537-857c-b4c849d41db9.PNG">
 
The metadata folder contains four pickle files that are provided to you to check your code 
after you complete the tasks.

### To complete the Epidemic Simulator tutorial, please, do the following steps:
1. Clone the directory or download in ZIP format.
2. Read the SEIR_simulator_workshop_material.pdf to complete four tasks.
   1. Write update_coordinate function in the file particles.py
   2. Write plot function in the file particles.py
   3. Write transition function susceptible_to_exposed in the simulator.py
   4. Write transition function infected_to_recovered in the simulator.py

To check your code, please, run the files particles.py and simulator.py, respectively. 
In case of the correct answer, "Successfully passed" message will be printed.

## References:


A.	Kuzdeuov et al., "A Network-Based Stochastic Epidemic Simulator: Controlling COVID-19 With Region-	Specific 	Policies," in IEEE Journal of Biomedical and Health Informatics, vol. 24, no. 10, pp. 2743-	2754, Oct. 2020, doi: 	10.1109/JBHI.2020.3005160.

B.	Kuzdeuov, A. Karabay, D. Baimukashev, B. Ibragimov, and H. A. Varol, “Particle-based covid-19 simulator 	with contact 	tracing and testing,” medRxiv, 2020. [Online]. Available: https: 	//www.medrxiv.org/content/early/2020/12/08/2020.12.07.20245043

A.Karabay, A. Kuzdeuov, M. Lewis and H.A. Varol, “A Vaccination Simulator for COVID-19: Effective and    	Sterilizing 	immunization cases”, medRxiv, 2021. [Online]. Available: 	https://www.medrxiv.org/content/10.1101/2021.03.28.21254468v1.full

Link to the Github repository for the original Matlab source code files:

https://github.com/IS2AI/Particle-Based-COVID19-Simulator


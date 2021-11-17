# Tutorial on COVID-19 particle-based Epidemic Simulator
 
In this tutorial, we will implement a program that simulates 
the spread of the COVID-19 epidemic. We will work on a particle-based SEIR simulator 
where SEIR is the abbreviation of the four main epidemic states of a particle:
susceptible, exposed, infected, and recovered. 

## How to use? 

git-clone or download the package. The scripts and folders should be saved in the same directory. 

SEIR_simulator_material.pdf contains the material on particle model, simulator structure, and programming tasks.
The metadata folder contains four pickle files that are provided to you to check your code 
after you complete the tasks.

We recommend to watch the videos below before diving into the tutorial. 

### Requirements:

1. Anaconda3 (with Jupyter included):
 https://docs.anaconda.com/anaconda/install/
2. Spyder IDE:
 https://www.spyder-ide.org


Download the sim_env.yaml file and create a new environmnent in the Anaconda terminal:

     conda-env create -n sim_env -f  \path\to\sim_env.yml

Activate sim_env:
     conda activate sim_env

Run the Spyder IDE in the sim_env environment. 


## Step 1. The following video provides the overview of the simulator, the particle model and the epidemic state transitions. 
Click on the image below to watch the video.

[![video_1](https://github.com/IS2AI/tutorial_COVID-19_epidemic_simulator/blob/main/imgs/Part_1.png)](https://www.youtube.com/watch?v=dUnBlSSeAf4&list=PLYwixe_5vr_m5GpohU4sf7-36IpysZx3f&index=3&ab_channel=ISSAI_NU)

## Step2. The next video introduces the code structure.

[![video_2](https://github.com/IS2AI/tutorial_COVID-19_epidemic_simulator/blob/main/imgs/Part_2.png)](https://www.youtube.com/watch?v=Cj53A-yoXiM&list=PLYwixe_5vr_m5GpohU4sf7-36IpysZx3f&index=4)

## Step3. The following video contains four programming tasks with solutions.

The tasks

[![video_3](https://github.com/IS2AI/tutorial_COVID-19_epidemic_simulator/blob/main/imgs/Part_3.png)](https://www.youtube.com/watch?v=j-aov6DRRTU&list=PLYwixe_5vr_m5GpohU4sf7-36IpysZx3f&index=5)


## References:

B.	Kuzdeuov, A. Karabay, D. Baimukashev, B. Ibragimov, and H. A. Varol, “A Particle-based covid-19 simulator 	with contact 	tracing and testing,” medRxiv, 2020. [Online]. Available: https: https://ieeexplore.ieee.org/document/9372866

A.Karabay, A. Kuzdeuov, M. Lewis and H.A. Varol, “A Vaccination Simulator for COVID-19: Effective and    	Sterilizing 	immunization cases”, medRxiv, 2021. [Online]. Available: 	https://ieeexplore.ieee.org/document/9542855

Link to the Github repository for the original Matlab source code files:

https://github.com/IS2AI/Particle-Based-COVID19-Simulator


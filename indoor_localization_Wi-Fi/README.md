# ISSAI-AUA-Summer-School

A Tutorial on WiFi-based Indoor Localization 

The task of localization aims to determine a user’s (or an object’s) position in space. It is essential for a variety of applications (i.e emergency response, health care and public safety). While the outdoor localization problem was solved by the global navigation satellite systems (GPS, GLONASS and GALILEO), the indoor localization still remains an open problem.

In this tutorial, we will use the simplified version of the [WiFine dataset](https://github.com/IS2AI/WiFine) to train a location prediction model. 

The following video provides an introduction to the problem of indoor localization, our solution and the WiFine dataset.
    
The video is followed up by the programming part, which is divided into two Jupyter Notebooks:
1. *indoor_localization_parts_1_2.ipynb*. 
    - Contains tasks on loading and preprocessing the dataset. 
    - Walks through predicting of a user's coordinates using randrom forest regression.
3. *indoor_localization_parts_3.ipynb*. 
    - Introduces a simple multi layer perceptron to predict a user's coordinates

Note, the target values for the test set are withheld. Instead, you are given the validation set to verify your best estimator.

Feel free to experiment with the code we provided or come up with a different approach. If you want to know how well you did on the test set, email us (<font color=blue>issai@nu.edu.kz</font>) your code and the predictions of your best estimator on the test features! 

The best mean error distance we got so far is 1.44, we hope you can beat this record!


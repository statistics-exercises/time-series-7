import matplotlib.pyplot as plt
import numpy as np

def exponential(lam) :
  # Your code to generate an exponential random variable goes here
  

lamd = 2  
number_of_events = np.zeros(100)
arrival_times = np.zeros(100)
for i in range(100) : 
  # You need to write code in here in order to set the elements 
  # of the two lists number_of_events and arrival_times
  
  
plt.plot( arrival_times, number_of_events, 'ko' )
plt.xlabel("time")
plt.ylabel("number of events")
plt.savefig("poisson.png")
  

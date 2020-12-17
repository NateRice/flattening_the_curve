# -*- coding: utf-8 -*-
"""
Author: Nathan Rice
Flattening the Curve
Using SIR model for spread of disease from epidemiology 
to model effects of different levels of disease spread prevention measures
(value of Rnot is infection reproduction value)
"""
import matplotlib.pyplot as plt
import numpy as np

def sirModel(x):
    '''Generates plot for SIR model using parameter value for Rnot'''
    # lists to save values of S, I, and R after each hour
    S_day = []
    I_day = []
    R_day = []
    
    gamma = 20*24 #typical recovery time in hours
    Rnot = x #basic reproduction number of an infection
    #Iof0
    I = 100000 #number of infections on day 0 - March 29 2020
    #Rof0 =  0 recovered
    R = 0
    P = 300000000 #total population of the United States
    #Sof0 = P - Iof0 #susceptible
    S = 299900000
    
    hours = list(range(7200))
    
    for t in hours:
        #print("\nt = ",t)
       
        # _now variables are S, I, R at time t
        S_now = S
        I_now = I
        R_now = R
        
        # S, I, and R are now known at time t+1
        I = I_now + ((Rnot*I_now*S_now)/(gamma*P)) - (I_now/gamma)
        I_day.append(I)
        S = S_now - ((Rnot*I_now*S_now)/(gamma*P)) 
        S_day.append(S)
        R = R_now + (I_now/gamma)
        R_day.append(R)
        #print("S+I+R = %f"%(S+I+R))
        #print("S_day = ",S_day)
        #print("I_day = ",I_day)
        #print("R_day = ",R_day)
    print("Maximum people infected for rnot value = ",x,":",round(max(I_day)))            
    
    sarr = np.array(S_day)
    iarr = np.array(I_day)
    rarr = np.array(R_day)
    hoursarr = np.array(hours)
    days = hoursarr/24
    
    plt.plot(days, sarr, 'b-')
    plt.plot(days, iarr, 'r-')
    plt.plot(days, rarr, 'g-')
    plt.yscale('linear')
    plt.xscale('linear')
    plt.xlabel('Days')
    plt.ylabel('Number of People in hundreds of millions')
    plt.legend(['Susceptible','Infected','Recovered'])
    string_for_title = "SIR model for infection reproduction value " + str(x)
    plt.title(string_for_title)
    name_of_plot = "rnot"+str(x)+".png"
    plt.savefig(name_of_plot,bbox_inches="tight")

sirModel(10)
plt.clf()
sirModel(4)
plt.clf()
sirModel(1.7)
        
#Maximum people infected for rnot value =  10 : 201,288,775
#Maximum people infected for rnot value =  4 : 121,176,853
#Maximum people infected for rnot value =  1.7 : 29,959,267

    
    


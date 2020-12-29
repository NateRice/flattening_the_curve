# "Flattening the Curve": _How to stop the spread of infectious diseases such as the coronavirus_ 
_Visualization of the coronavirus "flattening of the curve" based on the SIR model of disease spread 
used in the study of epidemiology. Coded in Python using pyplot and numpy. (Python program used to 
implement the model is SIR.py located in the ftc_files folder)_

#### Author: Nathan Rice

---

# Overview
The Rnot value, or reproduction value, in the SIR model is a measure of the reproduction rate of the 
disease. The lower the Rnot value, the less the disease is able to spread and infect people. We can think 
of preventative measures of disease spread such as social distancing, wearing a mask, and staying at 
home as representing a low Rnot value. In this way we can see the effectiveness of preventative measures 
on reducing the maximum number of people infected and slowing the rate of infection.

This model uses a typical recovery time of 20 days, an initial number of infections on day 0 of 100,000
as recorded on March 29, 2020, and the total population in the United States as 300,000,000.

# Visualization

A reproduction value of 1.7 could represent a situation where everyone always takes every preventative 
measure possible such as social distancing, wearing a mask, staying at home, and washing hands.

<p align="center">
   <img src="ftc_files/rnot1.7.png" width="600px">
</p>
The maximum number of people infected for rnot value 1.7 is 29,959,267.

A reproduction value of 4 could represent the population taking only some preventative measures, such as
wearing a mask and washing hands.

<p align="center">
   <img src="ftc_files/rnot4.png" width="600px">
</p>
The maximum number of people infected for rnot value 4 is 121,176,853.

A reproduction value of 10 represents a society where few people take preventative measures.

<p align="center">
   <img src="ftc_files/rnot10.png" width="600px">
</p>
The maximum number of people infected for rnot value 10 is 201,288,775.

# Results
When the preventative measures are taken seriously the infectious disease can be kept in check. With all
preventative measures taken, as represented by Rnot value 1.7, the maximum number of people infected is
171,329,508 less than when no preventative measure are taken, represented by Rnot value 10. Even with 
only some of the preventative measures in place, the maximum number of people infected is almost cut in
half. The speed at which the disease spreads is also greatly affected by the preventative measures. 
When all preventative measures are taken, the disease reaches the maximum level of infected after day 200.
When none of the preventative measures are taken, the maximum number of infected is reached after 50 days.

Using the SIR model of infectious disease spread this analysis has shown that taking measures to prevent
the spread of a disease can significantly slow the spread of the disease and reduce the maximum number of
people infected by the disease.
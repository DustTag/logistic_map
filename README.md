# Logistic Map

# This Repository includes 2 files that visually describe the chaotic behaviour of the Logistic Map.

# First file: bifurction_diagramm.py includes several functions that construct the bifurcation diagram of the Logistic Map. 
# User may: 
# 1. Tweak the range of value r by changing the interval variable.
# 2. Change The Accuracy of the drawing by changing the accuracy variable (Note: This action is recommended for small intervals, otherwise the drawing proccess will take a substantial amount of time)
# 3. Set the value of variable equal_aspect to either True or False. The User May want to do this for closer observations over a small interval (E.g. The Island of stability around r = 3.83)
# Side Note: The User May also change the colour of the diagramm by changing the "k." parameter in line 16. Note that regardless of your clour choice, the colourcode letter must always be followed up with dot (E.g. "k.", "b."). For colour references visit the following link: https://matplotlib.org/stable/users/explain/colors/colors.html 

# Second file: values_oscilations.py is intended for observing the behaviour of values Xn after several (80 by default) iterations.
# User may observe the folowing types of behaviour: 
# 1) Xn aproaches 0;
# 2) Xn aproaches a fixed point
# 3) Xn oscilates with a period being a power of 2;
# 4) Xn has chaotic behaivior
# 5) Xn oscilates with a period devisible by 3 and a power of 2 (island of stability)

# This code is open-source, so feel free to borrow it. Further additions and efficiency tweeks are highly appreciated.

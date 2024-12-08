# Strontium88
This is a simple Python Script to calculate the strontium transitions with cooling and trapping parameters. The code is heavily object oriented because of its suitability in repeated calculations with tunable parameters.

All the data concerning the transition wavelengths and matrix elements have been taken from official National Institute of Standards and Technology (NIST) data. The data can be viewed in the following paper: 
By all means, this python script does not contains all the Strontium 88 transitions but includes the ones which are either commonly used or have a large contribution in calculations of those commonly used transitions. You can easily add the data in the process outlined below. I have demonstrated the basic functionality of the code and ways in which you may use this. 

# What can you do?
You can calculate the transitions to and from a particular state along with the wavelengthts(nm) and dipole matrix elements(Atomic units). You can calculate the lifetime of states, Polarisability and width of transitions for two particular states. You can also calculate MOT and dipole trapping parameters in the semi-classical two-state model. 

# Basic Code Structure
There are two classes named as SR and LASER. All the calculations are done using the methods of the SR class. The objects of the SR class is the states of the atom on which you want to perform calculations. If you are not calculating the MOT and Optical dipole trapping parameters, this is the only class you'll need. The LASER class defines the laser as an object and will be used for MOT and Dipole Trap Calculations. 
To define a state, invoke the SR class which takes in the outermost 2 electron configuration, S, L and J (in units of hbar) in this particular order as strings. For example:

state1 = SR('5s5s','0','0','0') is the 5s2 state with S,L,J as 0.

To define the laser invoke laser class which takes in the width of the gaussian in mm, wavelength in nm and Power in mW. These odd units are taken because these are the orders of magnitudes in usual calculations. For example:

laser1 = LASER(6,690, 50) which means 6mm width 50 mW laser at 690 nm. You must note that the Gaussian width is the one you get after you place all the lenses and the atom is trapped.

# Calculate Transitions in and out of state

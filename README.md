# strontium88
This is a simple Python project made of two scripts to calculate the strontium transitions with cooling and trapping parameters. The code is heavily object oriented because of its suitability in repeated calculations with tunable parameters. 

Other sophisticated codes exist to calculate the parameters like this does but they are usually slow, are complex to understand and do the calculations by calculating wavefunctions and they were a overkill for my PhD project! Therefore I wrote something easy and light which every AMO physicist requires to calculate but has to do either rely on those big sophisticated codes or do them by hand!
They however do have their relevance in other aspects!

All the data concerning the transition wavelengths and matrix elements have been taken from official National Institute of Standards and Technology (NIST) data. The data can be viewed in the following paper: 
By all means, this python script does not contains all the Strontium 88 transitions but includes the ones which are either commonly used or have a large contribution in calculations of those commonly used transitions. You can easily add the data in the process outlined below. I have demonstrated the basic functionality of the code and ways in which you may use this. 
>[!NOTE]
>I have outlined the basic process of running in the **terminal**. The process to run it in IDE terminal is fairly easy. Just make sure the directory is correct. If you want to change directory, type in the IDE terminal,
>
>`import os`
>
>`os.chdir('the_path_to_folder')`
>
>Here you replace it with the path

Now you can simply go to section Basic Code Structure.

# What can you do?
You can calculate the transitions to and from a particular state along with the wavelengthts(nm) and dipole matrix elements(Atomic units). You can calculate the lifetime of states, Polarisability and width of transitions for two particular states. You can also calculate MOT and dipole trapping parameters in the semi-classical two-state model. 

# The Data and Units
The sr.data file contains all the information required to perform the necessary calculations. The commonly used units like the SI, FPS, MKS are not used here simply the atomic physics has its own set of units which are generally encountered. I have tried to consistently follow the below mentioned units. In the following section, I will refer to them as the standard units (please ignore my abuse of such terms). If no units are mentioned in front of the output, you can simply assume the below units for that:

Wavelength - nm

Dipole Matrix Elements: Atomic Units (charge on an electron * Bohr radius)

Frequency: MHz

Time: $\mu s$

Power: mW

distance: mm

# Where to start?
First of all, ensure that you have the correct folder added in path. If you are not aware of how to do it, just copy the path of the folder and write

`cd the_path_to_folder`

you replace the_path_to_folder with the actual path you copied.

Now you must ensure that numpy library is installed. After that you are good to go! Now just write

`python -i calc.py`

You will see an introduction comments and you can just start calculating.

# Basic Code Structure
There are two classes named as SR and LASER. All the calculations are done using the methods of the SR class. The objects of the SR class is the states of the atom on which you want to perform calculations. If you are not calculating the MOT and Optical dipole trapping parameters, this is the only class you'll need. The LASER class defines the laser as an object and will be used for MOT and Dipole Trap Calculations. 
To define a state, invoke the SR class which takes in the outermost 2 electron configuration, S, L and J (in units of hbar) in this particular order as strings. For example:

`state1 = SR('5s5s','0','0','0') `

is the 5s2 state with S,L,J as 0.

To define the laser invoke laser class which takes in the width of the gaussian in mm, wavelength in nm and Power in mW. These odd units are taken because these are the orders of magnitudes in usual calculations. For example:

`laser1 = LASER(6,690, 50)`

which means 6mm width 50 mW laser at 690 nm. 
>[!CAUTION]
>The Gaussian width is the one where atom is placed after the optical arrangements and not the width at the laser source.

# Calculate Transitions in and out of state
After you have defined the states, now we can play with it! You can easily find the transitions connecting with the state you defined. Transition from a state here means that all the states which have energy higher than the state mentioned with a finite dipole matrix element. Transition to a state means that all states which are lying low below the defined state with a finite matrix elements. Use the code
`SR.TransitionFrom(state1)` and `SR.TransitionTo(state1)`.

# Calculate Width of Transition
Define another state (instance of the SR class). Calculate the resultant **width in MHz** by


`SR.TransitionLinewidth(state1,state2)`


>[!CAUTION]
> state1 should be lower in energy than state2

# Atomic Linewidth and Lifetime
By summing over all linewidths for state1, one can find Natural width and the lifetime. Use 

`SR.TotalLinewdith(state1)`

Invert the number and divide by $2 \pi$ and you get the lifetime in $\mu s$.

# Polarizability
One can also get very accurate results on Polarisability of the state in SI units. Use 

`SR.Polarisability(stat1, wavelength-in-nm)`

You can also calculate the DC Polarisability by writing np.inf in the wavelength-in-nm place.

# Laser Class and Interaction of Lasers with Atoms
All of the above methods did not use the laser profile for calculations. However, when you want to study the interaction of coherent radiation with atoms, specifically in trapping and cooling atoms, we want to employ the laser properties. We assume that the laser to be a Gaussian TEM 00 mode and is defined by its beam width, Power and wavelength in standard units (not SI!) and in free space. To invoke the laser class, we define it by

`laser1 = LASER( beam width, wavelength, power)` 

Where you enter the floating inputs and not strings. Defining the laser will also print the Rayleigh Range for the user's convenience and verifying the validity of Ray optics in their calculations. 

# MOT parameters
Some essential parameters can also be calculated using the method MOT. Let the lower state be state1 and the higher state be state2. The user just needs to invoke the MOT class and all the important MOT parameters will be printed. The method can be invoked by typing in

`MOT(state1, state2, laser1)`

The user will be returned:

**Capture Velocity** and corresponding energy which is the range of atom's motional velocity within which the MOT acts as an optical molasses with a $-b \vec{v}$ dissipative force. 

The value of $s_0$ which is the **on-resonance saturation parameter** defined by $I/I_s$ where $I_s$ is the saturation intensity.

The minimal achievable **Doppler Temperature** and the **optimal doppler detuning**.

The detuning of the laser defined by the user. 

# Dipole Trap Parameters

Similary, one can also calculate the Optical Dipole Trap parameters by invoking the class 

`DipoleTrap(state1, state2, laser1)`

We will get the following data:

The **Trap Depth**.

The **Trap Frequencies** along the laser beam and in the direction perpendicular to it. 

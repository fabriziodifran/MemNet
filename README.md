# MemNet_1
This repository contains code to simulate square-shaped memristive arrays of an arbitrary size*. 
The size (N) is determined by the number of nodes of each side in a matrix geometrical array. 
Every two consecutive nodes, one memristive unit is placed either along horizontal or vertical directions.  
The model determining each memristive unit's behaviour has been adapted from previously developed models: 

> Y. V. Pershin and M. Di Ventra, 'SPICE model of memristive devices with threshold', Radioengineering 22, 485 (2013).
> 
> I. Vourkas and G. Sirakoulis, 'Memristor-Based Nanoelectronic Computing Circuits and Architectures' (Springer, 2015).

This code has been used to generate data for the manuscript

> F. Di Francesco, G.A. Sanca, and C.P. Quinteros. 'Spatial emerging texture in simulated memristive arrays'. https://arxiv.org/submit/3880033

*Although arbitrary sizes are allowed, the simulation is not optimized for big sizes (N>50) making the code time-consuming. 
Further versions will deal with this issue. 

## Requirements
Python 3 is used to set the array. Numpy and Pandas packages are required.
NGSPICE is the engine required for individual unit's simulation. 

## Getting started
Download the full repository and make sure NGSPICE is path-available (callable from Python scripts). 

Set the parameters by editing params.py and run main.py. 

A folder named exported_data will be created and two outputs files will be displayed: 

> simulation_iv 
> > containing three columns: time, current, and voltage (the latter two measured at the source)
> > 
> simulation_states
> > containing N x N + 1 columns: time, X(0 0), X(0 1), ..., X(N-1 N-1) 
> > 
> > being X(i j) the internal state of the unit whose cathode is connected to node (i j)   

For further questions email us at cquinteros@unsam.edu.ar.

## License
This code is for non-commercial use under a CC BY license (Creative Commons Attribution 4.0 International License).

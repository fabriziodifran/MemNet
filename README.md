# MemNet_1
This repository contains code to simulate square-shaped memristive arrays of an arbitrary size. 
The size is determined by the number of nodes of each side in a matrix geometrical array. 
Every two consecutive nodes one memristive unit is placed either along horizontal or vertical directions.  
The model determining each memristive unit's behaviour has been adapted from previously developed models: 

> Y. V. Pershin and M. Di Ventra, 'SPICE model of memristive devices with threshold', Radioengineering 22, 485 (2013).
> 
> I. Vourkas and G. Sirakoulis, 'Memristor-Based Nanoelectronic Computing Circuits and Architectures' (Springer, 2015).

This code has been used to generate data for the manuscript

> F. Di Francesco, G.A. Sanca, and C.P. Quinteros. 'Spatial emerging texture in simulated memristive arrays'. ArXiV 

The outputs contain all the necessary data to generate the figures of such communication. 

## Requirements
Python 3 is used to set the array. NGSPICE is required for individual unit's simulation. 

## Getting started
Two directories are available. They correspond to the simulation of an individual memristive unit and a memristive array, respectively.

For further details check the instructions within the corresponding directories. 

%%% Acá pongo lo que repartiría en los correspondientes README dentro de cada subdirectorio %%%
For individual unit's simulation:

xxx

The output is an ASCII file containing the variables: time, current, voltage, and memristive internal state.

For network generation and electrical simulation: 

xxx

Available parameters can be set using parameters.py. Run the scripts in the following order

Two ASCII files are generated as outputs: 

> simulation_iv comprising the variables: time, source current, and source voltage
> 
> simulation_state including time and the internal state of each unit labeled as the nodes between which each one is connected 

%%%%%%%%%%%

## License
This code is for non-commercial use under a CC BY license (Creative Commons Attribution 4.0 International License).

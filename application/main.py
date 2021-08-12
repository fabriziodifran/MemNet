from netlist_generation import SpiceNetlist
from network_generation import Network
import numpy as np
import os

from export_data import data_export
from constants import BASE_FILENAMES, FILEPATH, REPO_PATH
import params

# pwl generation
def _pwl_generation():
    f = open(f"{FILEPATH}/vsource.txt", "w")
    time = np.linspace(params.tstart, params.tstop, 1000)
    voltage = -abs(params.amplitude * np.sin(2*np.pi*params.freq*time))
    file_lines = ""
    for t, v in zip(time, voltage):
        file_lines += f"{t} {v} "
    f.write(f"pwl ({file_lines})")
    f.close()

if 'tmp_data' not in os.listdir():
    os.mkdir('tmp_data')
if 'exported_data' not in os.listdir():
    os.mkdir('exported_data')

state_list = []
_pwl_generation()
    
network = Network().generate_network()
netlist = SpiceNetlist()
netlist.generate_netlist(network, f"{BASE_FILENAMES}_0")
netlist.run_ngspice(f"{BASE_FILENAMES}_0")
state_list.append(netlist.state_nodes) 

data_export(state_list, 1)


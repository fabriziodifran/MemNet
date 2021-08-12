import os
import numpy as np

import params
from constants import FILEPATH


class SpiceNetlist():

    def __init__(self):
        self.connections = []
        self.state_nodes = []
    
    def generate_netlist(self, network, netlist_name, sensibilize_params={}):
        for edge in network.edges:
            node1 = edge[0]
            node2 = edge[1]
            gnd_node = self._get_gnd_node(network, params.network_dimention)
            voltage_input_node = list(network.nodes)[0] 
            
            n1 = f"n{node1[0]}{node1[1]}"
            n2 = f"n{node2[0]}{node2[1]}"

            if node1 == voltage_input_node:
                n1 = "vin"
                
            if node1 == gnd_node:
                n1 = "gnd"
                
            if node2 == gnd_node:
                n2 = "gnd"
            
            self.state_nodes.append(f"L({node1[0]};{node1[1]})({node2[0]};{node2[1]})")
            self.connections.append((n1,n2))
        
        self._write_netlist_file(self.connections, netlist_name, sensibilize_params)

    def run_ngspice(self, netlist_name):
        os.system(f"ngspice {FILEPATH}/{netlist_name}.cir")

    def _get_gnd_node(self, graph, N):
        last_row_nodes = []
        for node in graph.nodes:
            if str(N-1) in str(node[0]):
                last_row_nodes.append(node)
        return last_row_nodes[0]


    def _write_netlist_file(self, connections, netlist_name, sensibilize_params):
        states = ""
        f = open(f"{FILEPATH}/{netlist_name}.cir", "w+")   
        f.write("Memristor Random network \n")
        f.write(f".include ../models/{params.model}.sub\n")
        vin = self._get_vin_type()
        f.write(f"V1 vin gnd {vin}\n")
        
        for idx, c in enumerate(connections):
            alpha = params.alpha
            beta = params.beta
            vt = params.vt
            Roff = params.Roff
            ratio = params.ratio
            p_high_state_init = params.p_high_state_init
            Rinit = np.random.choice((Roff/ratio, Roff), p=[1-p_high_state_init, p_high_state_init]) 
            
            model_params = f"alpha={alpha} beta={beta} Roff={Roff} Ron={Roff/ratio} Rinit={Rinit} Vt={vt}"
            
            f.write(f"Xmem{idx} {c[0]} {c[1]} l{idx} memristor {model_params}\n")
            states += f"l{idx} "

        f.write(f".tran {params.tstep} {params.tstop} {params.tstart} uic\n")
        f.write(".control\n")
        f.write("run\n")
        # f.write("option numdgt=7\n")
        f.write("set wr_vecnames\n")
        f.write("set wr_singlescale\n")
        f.write(f"wrdata {FILEPATH}/{netlist_name}_states.csv " + states + " \n")
        f.write(f"wrdata {FILEPATH}/{netlist_name}_iv.csv i(v1) vin\n")
        # f.write("plot -i(v1) vs vin\n")
        f.write("quit\n")
        f.write(".endc\n")
        f.write(".end\n")
        f.close()

    def _get_vin_type(self):
        if params.v_type == "sine":
            return f"sin (0 {params.amplitude} {params.freq}"
        elif params.v_type == "pwl":
            f = open(f"{FILEPATH}/vsource.txt", "r")
            pwl = f.read()
            return f"{pwl}"

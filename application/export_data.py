import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from constants import BASE_FILENAMES, FILEPATH, REPO_PATH

def _create_sim_folder():
        actual_time = datetime.now().strftime("%d-%m-%Y_%H%M%S")
        dir_path = f"{REPO_PATH}/exported_data/{actual_time}"
        os.mkdir(dir_path)
        return dir_path

def data_export(states, no_of_simulations):
    simulation_dir = _create_sim_folder()
    for i in range(no_of_simulations):
                data_iv = pd.read_csv(f"{FILEPATH}/{BASE_FILENAMES}_{i}_iv.csv", sep="\s+")
                data_iv.columns = ["time", "current", "voltage"]
                data_states = pd.read_csv(f"{FILEPATH}/{BASE_FILENAMES}_{i}_states.csv", sep="\s+")
                data_states.columns = ["time"] + states[i]
                
                data_iv.to_csv(f"{simulation_dir}/{BASE_FILENAMES}_{i}_iv.csv", sep=",", header=True, index=False)
                data_states.to_csv(f"{simulation_dir}/{BASE_FILENAMES}_{i}_states.csv", sep=",", header=True, index=False)
# Network parameters
network_dimention = 4
model = "pershin"
p_high_state_init = 1

# Spice Vin parameters
v_type = "sine"
amplitude = 10.0
freq = 1

# Spice simulation parameters
samples = 1500
tstop = 3
tstep = tstop/samples
tstart = 1e-9

# Pershin's model parameters
Roff = 2e5
ratio = 100
vt = 0.6
beta = 5e5
alpha = 0

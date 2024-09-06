import matplotlib.pyplot as plt
import numpy as np


# Generating a line chart for the equation E= N(20ms+3*L)

# Constants
T_app_in_ms = 20
redis_ops_per_call = 1

# Range for N (number of times)
N_values = np.arange(1, 101)  # From 1 to 100

# Latencies for line chart
latencies = [1, 50, 100, 150,175, 200]

# plot dime
plt.figure(figsize=(12, 8))

for L in latencies:
    E_values = T_app_in_ms + N_values * (redis_ops_per_call*L)
    plt.plot(N_values, E_values, label=f'Latency = {L} ms')

plt.title('Total Time (T) vs. Number of Operations (N) for Different Latencies')
plt.xlabel('Number of Operations (N)')
plt.ylabel('Total Time (T) in milliseconds')
plt.legend()
plt.grid(True)
plt.savefig('output.png')

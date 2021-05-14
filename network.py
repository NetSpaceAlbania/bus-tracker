"""
Simulimi i rrjetit te komunikimit midis pajisjeve

Potential issues:
    network management
    collection of coordinates
    implementation of gateways
    microcontrollers
    decentralized network
    Global Positioning System
    LoRA range
    Stations far apart
    Tracking the moment when bus reaches at least one station
    best aalternatives to buld the network? GPS, LoRA
    Energy consumption bluetooth, wifi. Source solar panels
    proper device setup
    edge cases/scenarios i.e. buses one after another at opposite sides
    model scenarios
    communication frequencies, bus stop, bus module freq tuner
    ETA, time calculations behind the model
    testing existing solutions, maps APIs and mobile phone GPS
    proper plan and team for the project
    what is the simplest solution to start off with


"""

import time

# Komunikimi midis tre nyjeve
i = 0
while i <= 11:
    node1 = "hello"
    i += 1

    print(node1)

node2 = 2

node3 = 3

def probability():
    # Random variable representing number of buses
    # Random variable representing number of buses
# Mean number of buses coming to bus stop in 30 minutes is 1
#
X = [0, 1, 2, 3, 4]
lmbda = 1
#
# Probability values
#
poisson_pd = poisson.pmf(X, lmbda)
#
# Plot the probability distribution
#
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, poisson_pd, 'bo', ms=8, label='poisson pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. of Buses", fontsize="18")
plt.title("Poisson Distribution - No. of Buses Vs Probability", fontsize="18")
ax.vlines(X, 0, poisson_pd, colors='b', lw=5, alpha=0.5)

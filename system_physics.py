import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class systemPhysics:


    def bus_physics():

        line = 1 # bus line
        speed = 1 # m/s
        time = 10 #seconds
        acceleration = 2 # dynamics
        bus_eta = 120 # estimated time of arrival at the station
        bus_number = 1 # bus number

        return bus_eta
    
    def plot_func(speed, distance):
        X = np.linspace(0, 2*np.pi, 100)
        Y = np.cos(X)

        fig, ax = plt.subplots()
        ax.plot(X, Y, color = 'C1')

        fig.savefig("figure.pdf")
        return fig.show()


physics = systemPhysics.bus_physics()

plotfunc = systemPhysics.plot_func()
plotfunc

print("bus transceiver {b_rxtx} and station transceiver {s_rxtx}")
# plot the data in matplotlib

print (f'bus arrives in {physics} minutes')

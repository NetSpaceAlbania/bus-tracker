from pysim.simulation import Sim
from pysim.systems import VanDerPol
import matplotlib.pyplot as plt

#Create a Simulation
sim = Sim()

#Create, set up and add a system to simulation
sys = VanDerPol()
sys.store("x")
sim.addSys(sys)

#Simulate and plot the results
sim.simulate(20,0.1)
x = sys.res.x
plt.plot(x)
plt.show()

class systemPhysics:


    def bus_physics():

        line = 1 # bus line
        speed = 1 # m/s
        time = 10 #seconds
        acceleration = 2 # dynamics
        bus_eta = 120 # estimated time of arrival at the station
        bus_number = 1 # bus number

        return bus_eta



physics = systemPhysics.bus_physics()
print (f'bus arrives in {physics} minutes')

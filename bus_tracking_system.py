# Classes and implemented functions for bus tracking system

"""
trackingSystem
    ...
    bus_module() # embedded module that will be installed in the bus
    gps_data() # data fetched and output from gps module
    stations() # storing information about previous and next station

    Simulator
    --------
    bus_physics() # physics for the simulator

"""
import time

class TrackingSystem:
    """
    A class used to simulate a bus tracking system

    ...

    Attributes
    ----------
    bus_number : int
        Explanatory message
    bus_line : int
        Explanatory message
    bus_driver : str, optional
        Explanatory message

    Methods
    -------
    bus_module()
        yields the data
    """    
    def __init__():

        """
        Parameters
        ----------
        bus_number : int
            Explanatory message
        bus_line : int
            Explanatory message
        bus_driver : str, optional
            Explanatory message

        Raises
        ------
        NotImplementedError
            If nothing...
        """

    def bus_module():
        """
        Bus module is the main embedded device that contains the hardware modules
        and will serve and fetch data with other modules installed in stations
        """
        # module identifier
        module_id = 1
        gps = "gps to yield lon, lat"
        wifi = "wifi to communicate with nearest station"
        rf = "rf to communication with next other lora (nrf211)"
        lora = 'wifi module to send receive data (ESP32)(ESP8266)'
        network_db = 'report to network database'
        bus_display = 'display next bus nr/line/next station'
        
        # This function will take care of the data
        return "bus module"

    def gps_data():
        """
        This module will be attached to the bus module
        """
        lon = '123'
        lat = '456'
        return (lat, lon)

    def eta():
        """
        This method will output the Estimated Time of Arrival of the bus to the station
        """
        est_time = time.ctime()
        return est_time

    def display():
        """
        Display panel mounted in the bus

        """
        print("I will take care displaying the bus line and next station")

    def stations():
        """
        This function will determine the next stations the bus is approaching
        """
        station_name = 1
        location = [30, 10]
        bus_number = 1
        estimated_time = 120
        # return approaching bus_number and time
        next_station = "fetch location, check direction, announce"

        return next_station

class SystemPhysics:

    def bus_physics():

        # line number denotes a specific bus trajectory
        line = 1 # a line may have many stations
        speed = 1 # m/s
        time = 10 # seconds
        acceleration = 2 # m/s^2
        direction = ['forward', 'backward']
        # estimated arrival time to the station
        arrival_time = 120
        bus_number = 1
        # return bus arrival time to the next station
        return arrival_time, bus_number

# Potential future functionality and features for the system
class Features:
    """
    Future features
    ----

    Voice enabled announcement system (next bus, issues/problems with bus lines)
    """

# methods from trackingSystem
bus = TrackingSystem.bus_module()
station = TrackingSystem.stations()
gps_data = TrackingSystem.gps_data()
eta = TrackingSystem.eta()
# methods from systemPhysics
physics = SystemPhysics()
# print('hello from system physics',physics)

print(f'bus {bus} is {eta} minutes way from station {station} at location {gps_data}')

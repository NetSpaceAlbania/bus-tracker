# Simulation of device communication

'''
simulation of communication devices from bus to station and vice-versa
b(rxtx) - bus transceiver
s(rxtx) - station transceiver


____b(rxtx)____________s(rxtx)_______________s2(rxtx)__



remote rxtx
_________s3(rxtx)____________


'''
def bus_rxtx():

    """
    bus rxtx
    """
    b_rxtx = 123.456

    return b_rxtx

def station_rxtx():
    
    """
    station rxtx
    """

    s_rxtx = 234.567

    return s_rxtx

print(f"bus transceiver information {bus_rxtx()} and station transceiver {station_rxtx()}")


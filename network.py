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
    
    payload = 'flag/deviceid/data/'
    msg = 'test1234'
    b_rxtx = 123.456
    tx = True
    rx = False

    return b_rxtx

def station_rxtx():
    
    """
    station rxtx
    """

    msg = 'test 123'
    tx = True
    rx = False

    s_rxtx = 234.567

    return s_rxtx


def net_estimator():
    """

    calculate device location in the network
    """
    # calculate device location
    dev_location = diff_txrx / timestamp
    
    return dev_location * 


print(f"bus transceiver information {bus_rxtx()} and station transceiver {station_rxtx()}")


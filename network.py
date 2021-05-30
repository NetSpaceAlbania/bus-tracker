"""
Simulimi i rrjetit te komunikimit midis pajisjeve

"""

import time

# Komunikimi midis tre nyjeve

"""
node 1 [id, data] - node2 [id, data]

"""

def nyja1():
    tx= True
    rx = False
    nid='nyja001'
    tstamp=time.time()
    data = 123
    status = 'not ack'
    packet=[nid,tstamp,data, status]

    print(packet)




if __name__ == '__main__':
    nyja1()
    #nyja2()
    #nyja3()

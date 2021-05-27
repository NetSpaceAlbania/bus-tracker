# Chapter2Model1Modified.py 
# Import arcpy module 
import numpy as np
import uuid

# bus station coordinates
l={'linja':'1','st1':'41.3, 19.1', 'st2':'41.3, 19.2', 'st3':'41.3, 19.3'}

st = len(l)

print(f"linja {l['linja']} ka {len(l)} stacione, vendndodhja e tanishme {l['st1']} ")


def genId():
    """
    Gjenerator per ID automatike
    """

    uid = uuid.UUID

    print (f"bus is assigend this unique id {uid}")

genId()

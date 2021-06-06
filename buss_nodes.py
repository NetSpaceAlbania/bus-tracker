
#this is the bus node ID 
# buss id = Bus nr , line nr , module ID
buss_id = ["BNr0","LNr0","BM0"]
#node list = list of nodes buss module should communicate 
node_list = ["SM00","SM01","SM02","SM03","SM08","SM09",]


#here geolocation variables should be added 
geodata :????????



# this class will be populated with communication data  
class start_sending:







#handshake to verify communication 
communication begin()

    #checker 
if node_id in node_list:
    start sending
    # buss_id,
    # bus_geolocation,
    # other_buss_data

else :
    communication drop the packets

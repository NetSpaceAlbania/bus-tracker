# this is the station node ID 
Station_id = ["SM00","SGeoloc","SNr00"]


#this is buss node list 
buss_node_list = ["LNr0","LNr5","LNr9","LNr13","LNr15","LNr18","LNr20","LNr22","LNr25","LNr30","LNr310","LNr40",]

#this will be the core data of the communication

buss_data = [buss_ID, buss_location ]


#this will be a hybrid mesh just for fun
#station_node_ list =["Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0","Nid0",]
 
#class data_to_be_send:
#   BNr
#   LNr
#   Statin nr.

#start communication between station nodes

#def start_sending_data:
#     data_to_be_send()

# class counter
# if more then 2 = LNr in stuck:
#       dorp the 3 one  



# this function  will gether data for all nodes in its range that are in the buss_node_list
def start_gethering:
    get_buss_id = "form input data get 'BNr' & 'LNr'"
    get_buss_location = "log lat speed other stuff"

#this function counts the distance form bus geolocation to station geolocation
def count_the_distance:
  print ("some magic math will happen here")

# this function sends data to gateway
def gateway_send:
    send_bussdata = buss_data[]
    send_node_data = Station_id


start communication to nodes {}

#checker 
if Buss_id not in buss_node_list:
    communication drop
else:
    distance = count_the_distance()
    print("autobuzi " + BNr + " i Linjes "+ LNr + " ndodhet " +distance+ " larg")



start communication to gateways {}


gateway_send()

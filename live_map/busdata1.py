from pykafka import KafkaClient
import geojson
from datetime import datetime
import uuid
import time

# read input date from geojson file
input_file = open('./data/linja1.geojson')
geojson_array = geojson.load(input_file)

print ("geojson", geojson_array)
coordinates = geojson_array['coordinates']

# generate uuid
def generate_uuid():
    return uuid.uuid4()

# start kafka
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata_final123']
producer = topic.get_sync_producer()

# format the message and send it to kafka
data = {}
data['busline'] = '00001'

def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        # reverse bus starting point once end busstop reached. 
        if i == len(coordinates)-1:
            i = 0
        else:
            i += 1

generate_checkpoint(coordinates)

Imagine splitting a monolithic system with a lot of microsystems 
cost a lot of interfaces, protocols to implement, interfaces , data schema 

kafka is a distributed fault tolerant mesagging system, high performace with latency and you can achieve real time messaging bus.

The applications can act as producers to certain topics as a stream of data so that applications can consume and produce data. 

[services] [*s1][*s2][*s3]
|
producer
|
_________________
[*bus data] kafka
_________________
|
consumer
|
[services] [*s4][s5][...]

Having this system setup in place can allow us implementing a consumer-producer application with leaflet.js with data in real-time. 


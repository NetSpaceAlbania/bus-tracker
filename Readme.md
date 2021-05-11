
# Projekti per gjurmimin e Autobuzave - Bus Tracker Project
Ky projekt buron dhe zhvillohet nga komuniteti i Hackerspace Albania qellimi i ketij projekti synon krijimin e nje sistemi te hapur informativ per udhetaret qe perdorin transportin publik.

Elementet e ketij projekti perbehen nga pajisje me baze IoT, Mikrokontrollera, Rrjeti i komunikimit dhe aplikacionet (shtresa software) qe mundeson nderfaqen me perdoruesit. Kontributi ne kete projekt mirepritet dhe mund te realizohet duke krijuar `pull request` nderkohe nese ju keni ide per sygjerime apo permiresime pa hezitim mund t'i beni `fork` tek github.

Instalimi i ketij projekti mundeson nisjen e nje modeli qe realizon nje simulim gjeografik te funksionit te pajisjeve, rrjetit dhe nderfaqes informative te perdoruesit. Per instalimin e projektit sygjerohen te ndermerren keto hapa (pamvaresisht sistemit te operimit):

1. git clone https://github.com/hackerspacealbania/bus-tracker.git
2. cd bus-tracker
3. docker-compose bustracker.yml


## IoT
-LoRA
-nrf24L
-Repeaters

Me teper detaje: documentation/
/bus_device.md
/bus_transceivers.md

- Gjurmim i bazuar ne RF
- Moduli kryesor LoRA TTGO T-Beam
- GPS, IMU

### Rrjeti
Komunikimi i pajisjeve ne rrjet eshte bazuar ne skeme hibride e cilat pershin topologji mesh-star-ring me aftesi shkeputjeje te modelit te topologjise ne menyre automatike.

`nodes-repeater and gateway-masternode`
-Nodes, modulet spiune te instaluar ne stacione
-Repeater, perfocruesi i komunikimit me rol te dyfishte si gateway
-Gateway, portat per rrjedhjen e informationit te grumbulluar
-Relays, rele rrjeti per optimizimin e ngarkeses se komunikimit ne rrjet


### Rrjeti

station_device.md
station_transceivers.md
- ttgo (geolocation)

# Logistics
system_scheduler.md
- Geolocation based system 
- Location estimation based on data

# Simulator

Kafka
leaflet.js

download apache kafka. Installing kafka requires java SE development kit. So ensure setting the environmnet variables [windows] properly adding them on the path (i.e. JAVA_HOME browse and include the directory you installed java). 

test installation

configure kafka directory, from installation directory:
i.e. /usr/local/Cellar/kafka/2.8.0/

## Comments
- Web-enabled simulator for simulating scenarios 
## future Steps
- Enable NFC cards
- Use USB powered electronics with 5V power level operation

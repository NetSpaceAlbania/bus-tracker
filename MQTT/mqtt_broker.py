"""

The Message Queueuing Telemetry Transport (MQTT) ky i fundit  eshte nje protokoll i konceptuar te punoje mbi nivelin TCP/IP per te mundesuar komunikimin midis pajisjeve. Metodika e komunikimit qe perdoret nga MQTT njihet si metoda Publish-Subscribe, PubSub.


"""


def gateway():
    """

    Gateway mundeson mbledhjet e komunikimeve nga pajisjet IoT pjese e rrjetit dhe
    shperndan keto te fundit tek tematikat e percaktuara ne MQTT broker per tek pajisjet qe jane te abonuara tek to.    
    """
    nodes = "numri i nyjeve raportuese tek gateway"
    topics = "numri i tematikave te disponueshme"
    pubsub_state = "Vertete/Gabuar"
    gateway_devices = "pajisjet e lidhura ne gateway"

    return ("raportimin e mesazheve te mbledhura tek pajisjet e abonuara")


def mqtt_broker():
    """

    Koordinimi i komunikimit te mesazheve te marra nga pajisjet dhe transmetimi perkates i ture tek pajisjet e abonuara
    """

    pub_devices = "pajisjet publikuese ne hyrje"
    sub_devices = "pajisjet e abonuara ne dalje"
    topic_clients = "teresia e pajisjeve te lidhura tek tematikat"


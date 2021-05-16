"""
The scheduling system will be able to coordinate the bus timetable with other bus lines
"""
# burimi i te dhenatve per linjat
linjat = {
        "linja1":"https://opendata.tirana.al/sites/default/files/Linja%201.geojson",
        "linja2":"https://opendata.tirana.al/sites/default/files/Linja%202.geojson",
        "linja3":"https://opendata.tirana.al/sites/default/files/Linja%203.geojson"
        }




def linjat():
    """ 
    linjat ne sherbim
    
    """

    stacioni = '1, 2, 3'
    
    print(f"Ndodhet tek {stacioni}")


def tabelaOrareve():
    """Funksioni per afishimin e te dhenave
    *** Linja numer {x} mberrin per {x} min
    """
    
    linja = line[1]
    kpm = "3"

    print(f"linja {linja} mberrin ne {kpm} minuta")

tabelaOrareve()

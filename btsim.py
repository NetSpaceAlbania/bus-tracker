"""
The scheduling system for bus lines and their timetable
Sistemi i planifikimit te orareve per linjat dhe oraret e tyre
"""
# burimi i te dhenatve per linjat
linjat_db = {
        "linja1":"https://opendata.tirana.al/sites/default/files/Linja%201.geojson",
        "linja2":"https://opendata.tirana.al/sites/default/files/Linja%202.geojson",
        "linja3":"https://opendata.tirana.al/sites/default/files/Linja%203.geojson"
        }

oraret = {"linja1":"8:00, 9:00, 10:00", "linja2":"9:30, 10:30, 11:30", "linja3":"12:00, 12:30, 13:00"}

# TODO: Lexo te dhenat nga .geojson file bazuar tek linjat_db

# TODO: Kalo te dhenat tek funksioni per linjat


def linjat():
    """ 
    linjat ne sherbim
    
    """
    geojson_sample = {"lat_lon":"19.818005561828613, 41.32387791374622, 19.813199043273926, 41.32307218496387"}

    print(f"Te dhenat per linjen ndodhen ne: {linjat_db['linja1']},  koordinatat e stacioneve per linjen 1:\n {geojson_sample['lat_lon']}")

# TODO: Afisho linjat qe kalojne tek stacionet 1, 2, 3

def tabelaOrareve():
    """Funksioni per afishimin e te dhenave
    *** Linja numer {x} mberrin per {x} min
    """
    
    linja = 1
    kpm = "3"

    #print(f"linja {oraret['linja1']} mberrin ne {kpm} minuta")
    print(f"Oraret per linjen 1 :\n {oraret['linja1']}\n, {oraret['linja2']}\n, {oraret['linja3']}\n")

if __name__ == '__main__':
    linjat()
    tabelaOrareve()

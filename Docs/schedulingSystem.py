"""
The scheduling system will be able to coordinate the bus timetable with other bus lines
"""

def lines():
    line = 1
    line2 = 2
    line3 = 3

    line.stations = 3
    line2.stations = 5
    line3.stations = 7

    station = 'busy'
    station2 = 'free'
    station3 = 'busy'

    report = 'report to timetable'

def timeTable():
    current_time = '08:00'


    # return estimated bus time for the specific station, and next bus line
    return bus_line_arrival_time, next_bus_line


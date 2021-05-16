# Chapter2Model1Modified.py 
# Import arcpy module 
import arcpy 
import csv 

# Local variables: 
Bus_Stops = r"C:ProjectsSanFrancisco.gdbSanFranciscoBus_Stops" 
CensusBlocks2010 = r"C:ProjectsSanFrancisco.gdbSanFranciscoCensusBlocks2010" 
Inbound71 = r"C:ProjectsSanFrancisco.gdbChapter2ResultsInbound71" 
Inbound71_400ft_buffer = r"C:ProjectsSanFrancisco.gdbChapter2ResultsInbound71_400ft_buffer" 
Intersect71Census = r"C:ProjectsSanFrancisco.gdbChapter2ResultsIntersect71Census" 
 
# Process: Select 
arcpy.Select_analysis(Bus_Stops,  
                      Inbound71,  
                      "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'") 
# Process: Buffer 
arcpy.Buffer_analysis(Inbound71,  
                      Inbound71_400ft_buffer,  
                      "400 Feet", "FULL", "ROUND", "NONE", "") 
  
# Process: Intersect 
arcpy.Intersect_analysis([Inbound71_400ft_buffe,CensusBlocks2010],  
                         Intersect71Census, "ALL", "", "INPUT") 
 
dataDictionary = {} 
with arcpy.da.SearchCursor(Intersect71Census, ["STOPID","POP10"]) as cursor: 
    for row in cursor: 
        busStopID = row[0] 
        pop10 = row[1] 
        if busStopID not in dataDictionary.keys(): 
            dataDictionary[busStopID] = [pop10] 
        else: 
            dataDictionary[busStopID].append(pop10) 
 
with open(r'C:ProjectsAverages.csv', 'wb') as csvfile: 
    csvwriter = csv.writer(csvfile, delimiter=',') 
    for busStopID in dataDictionary.keys(): 
        popList = dataDictionary[busStopID] 
        averagePop = sum(popList)/len(popList) 
        data = [busStopID, averagePop] 
        csvwriter.writerow(data) 

print "Data Analysis Complete"

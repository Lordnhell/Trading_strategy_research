import csv

path = "testsheet.csv"

with open(path,"r",encoding="utf-8") as datasheet:
    
    totalarray = []
    
    for i in range(0,5):
        totalarray.append({'A':0,'C':0,'G':0,'T':0})
        
    print(totalarray)
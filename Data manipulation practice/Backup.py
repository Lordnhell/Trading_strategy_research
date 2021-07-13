#Python Workshop Assesment

import csv

path = "Superstore.csv"
path2 = "example2.txt"

totalsales = 0
totalprofit = 0

furnisales = 0
techsales = 0
officesales = 0

furniprofit = 0
techprofit = 0
officeprofit = 0

testval = 0
temp = 0
int(temp)

bst_sell = {}

float(totalsales)

with open(path,"r",encoding="utf-8") as datasheet:
    reader = csv.DictReader(datasheet)
    
    for row in reader:
        sales = float(row.get("Sales"))
        profit = float(row.get("Profit"))
        cat = row.get("Category")
        state = row.get("State")
        subcat = row.get("Sub-Category")
        qty = int(row.get("Quantity"))        
        
        totalsales = totalsales + sales
        totalprofit = totalprofit + profit
        
        if (cat == "Furniture"):
            furnisales = furnisales + sales
            furniprofit = furniprofit + profit
        elif (cat == "Office Supplies"):
            officesales = officesales + sales
            officeprofit = officeprofit + profit
        elif (cat == "Technology"):
            techsales = techsales + sales
            techprofit = techprofit + profit
            
        if state in bst_sell:
            if subcat in bst_sell[state]:
                temp = int(bst_sell[state][subcat]) + qty
                bst_sell[state][subcat] = str(temp)
                temp = 0
            else:
                bst_sell[state][subcat] = qty
        else:
            bst_sell.update({state:{subcat:qty}})
        
        #testval = bst_sell[state][subcat]
        
        
with open(path2,"w") as finaltext:
    finaltext.write("test"+"test")
    finaltext.write("test")
    finaltext.write("test")
    finaltext.write("test")
            
        
    print(round(totalsales,2))
    print(round(totalprofit,2))
    
    print("")
    
    print(round(furniprofit,2))
    print(round(furnisales,2))
    
    print("")
    
    print(round(techsales,2))
    print(round(techprofit,2))
    
    print("")
    
    print(round(officesales,2))
    print(round(officeprofit,2))
    
    for key1,value1 in bst_sell.items():
        print(key1 ," : ",value1) 
        finaltext.write(str(key1)+ " : "+ str(value1))
        
    print(testval)
    
    test1 = "Chairs"
    
    print(state)
    
    print(bst_sell[state][test1])

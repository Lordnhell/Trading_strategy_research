#Python Workshop Assesment

import csv

path = "Superstore.csv"
path2 = "Final_report.txt"

totalsales = 0
totalprofit = 0

catsales = {}
catprofit = {}

statesales = {}
stateprofit = {}

bst_sell = {}
bst_sell_final = {}

temp = 0
int(temp)
temp2 = 0
int(temp2)

float(totalsales)

with open(path,"r",encoding="utf-8") as datasheet:
    reader = csv.DictReader(datasheet)
    
    for row in reader:
        sales = round(float(row.get("Sales")),2)
        profit = float(row.get("Profit"))
        cat = row.get("Category")
        state = row.get("State")
        subcat = row.get("Sub-Category")
        qty = int(row.get("Quantity"))
        
        #total sales figure calculation
        totalsales = totalsales + sales
        #total profit figure calculation
        totalprofit = totalprofit + profit
        
        #getting sales by category
        if cat in catsales:
            catsales.update({cat:(catsales[cat] + sales)})
        else:
            catsales.update({cat:sales})
        
        #getting profit by category
        if cat in catprofit:
            catprofit.update({cat:(catprofit[cat] + round(profit,2))})
        else:
            catprofit.update({cat:(round(profit,2))})
        
        #getting profit by state
        if state in stateprofit:
            stateprofit.update({state:(stateprofit[state] + round(profit,2))})
        else:
            stateprofit.update({state:(round(profit,2))})
            
        #getting sales by state
        if state in statesales:
            statesales.update({state:(statesales[state] + round(sales,2))})
        else:
            statesales.update({state:(round(sales,2))}) 
            
            
        #The best-selling Sub-Category for each State 
        if state in bst_sell:
            if subcat in bst_sell[state]:
                temp = int(bst_sell[state][subcat]) + qty
                bst_sell[state][subcat] = str(temp)
                temp = 0
            else:
                bst_sell[state][subcat] = qty
        else:
            bst_sell.update({state:{subcat:qty}})    
    
    for bst_state,bst_subcat in bst_sell.items():
        temp2 = 0
        for key3 in bst_subcat:
            if (int(bst_subcat[key3]) >= int(temp2)):
                temp2 = bst_subcat[key3]
                bst_sell_final.update({bst_state:{key3:temp2}})
        
#Writing everything to a text file
        
with open(path2,"w") as finaltext:
    
    finaltext.write("\n ")
    finaltext.write("\n The Total Sales : $" +  str(totalsales))
    finaltext.write("\n The Total Profit : $" + str(totalprofit))
    finaltext.write("\n ")    
    
    finaltext.write("\n Sales for each Category")
    finaltext.write("\n ")
    for key,value in catsales.items():
        finaltext.write("\n " + str(key) +"    -    $" + str(value))
    
    finaltext.write("\n ") 
    finaltext.write("\n Profit for each Category")
    finaltext.write("\n ")    
    for key,value in catprofit.items():
        finaltext.write("\n " + str(key) +"    -    $" + str(value))     
    
    finaltext.write("\n ")
    finaltext.write("\n The Sales for each State")
    finaltext.write("\n ")    
    
    for key,value in statesales.items():
        finaltext.write("\n " + str(key) +"    -    $" + str(value))      
    
    finaltext.write("\n ")
    finaltext.write("\n The Profit for each State")
    finaltext.write("\n ")    
    
    for key,value in stateprofit.items():
        finaltext.write("\n " + str(key) +"    -    $" + str(value)) 
        
    finaltext.write("\n ")
    finaltext.write("\n The best-selling Sub-Category for each State")
    finaltext.write("\n ")
    
    for bst_state1,bst_subcat1 in bst_sell_final.items():
        finaltext.write("\n" + bst_state1 + "\n ")
        for key4 in bst_subcat1:
            finaltext.write("     " +str(key4)+ " : "+ str(bst_subcat1[key4]))
        

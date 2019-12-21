
#imports os modules
import os
import csv
import pandas as pd

#define variables
total_month =0
total=0
Avgchange=0
curvalue=0
prevvalue=0
changevalue=0
changevaluetotal=0
leastchange=0
greatestchange=0
changevaluesum=0

#define list to hold monthly changes
monthlychangelist=[]
monthlychangepermonthlist=[]
#define summary report list
summaryreportlist=[]

#out put file
result_list = []
election_results_file = os.path.join('../Resources/Budget_Results_Report.txt')

#set path to excel file
budgetcsvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#open excel file for read
with open(budgetcsvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
      
    #The total number of months included in the dataset
        total_month +=1
    #The net total amount of "Profit/Losses" over the entire period
        total=total + int(row[1])
        #set current value for the loop
        curvalue= int(row[1])
        monthvalue=(row[0])
             
        if prevvalue!=0:
          
            #caluculate the change valu
            changevalue=curvalue-prevvalue
            #Append change valu to loop
            monthlychangelist.append(changevalue)
            monthlychangepermonthlist.append({'month':monthvalue,'change':changevalue})
            #curvalue=nextvalue
           
        #Calculate the next previuos valur for the next  loop
        prevvalue=curvalue
        #print( (changevalue))
   # print()
    #find greatest value
    greatestchange=max(monthlychangelist)
    
    #find minimum value
    leastchange=min(monthlychangelist)
    #sum 
    
    changevaluesum=sum(monthlychangelist)

    #The average of the changes in "Profit/Losses" over the entire period
    Avgchange=changevaluesum/(total_month-1)

    #print(monthlychangepermonthlist)
        
    #Create Summary report
    summaryreportlist.append("Financial Analysis")  
    summaryreportlist.append("------------------------")   
    summaryreportlist.append("Total Months: "+str(total_month)) 
    #print("Average  Change: $"+str(Avgchange)) 
    summaryreportlist.append("Average  Change: $""{0:.2f}".format(Avgchange)) 
    #print("{0:.2f}".format(Avgchange))
  
    #print("Total Months: {total_month}".format(total_month=total_month))
   # print("Total: $ "+str(total))
    for row in monthlychangepermonthlist:
        
    #The greatest increase in profits (date and amount) over the entire period
        if row['change']== greatestchange:
            summaryreportlist.append("Greatest Increase in Profits: "+ row['month']+" ($" + str(row['change'])+")")
    for row in monthlychangepermonthlist:
          #The greatest decrease in losses (date and amount) over the entire period
        if row['change']== leastchange:
            summaryreportlist.append("Greatest Decrease in Profits: "+ row['month']+" ($" + str(row['change'])+")")


# Print output of election results
with open(file=election_results_file, mode='w') as write_results:
    for election_results in summaryreportlist:
        # Print to terminal
        print(election_results)
        # Write to file
        write_results.write("{item}\n".format(item=election_results))






  
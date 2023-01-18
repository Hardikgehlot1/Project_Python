<<<<<<< Updated upstream

#Importing Modules
import os 
import csv


# Define Path for the csv files
csvpath = os.path.join("Resources/budget_data.csv")


#Defining the variables and setting up them to zero or a blank list
Total_months = 0 
Net_Profit_loss = []
diff = 0 

# The Start Heading of the statement 
print("Financial Analysis")
print("-------------------------------------------")



#Reading csv
with open (csvpath, newline = "") as csvfile:
    budget_dataCsv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    budgetDatalist = [row for row in budget_dataCsv]          


#print the Total months  
print("Total months :" + str(len(budgetDatalist)))

#Reading csv
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    
    #Going over each line and adding 1 when the Total_months is 0 and then appending to the empty list    
    for line in reader:
        if Total_months==0:
            Total_months+= 1
        Net_Profit_loss.append(int (line[1]))


#printing the Net profit and loss
print("Net profit and loss: $" + str(sum(Net_Profit_loss)))

#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    diffs = []
    #Going over to each lines and append to the prof_los empty list
    for line in reader:
      prof_los.append(int(line[1]))
    #Creating try catch statements 
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = abs(prof_los[index]) - abs(prof_los[index-1])
        diffs.append(diff)
      except Exception:
        continue
        #Finding average and assigning it to a variable then printing
    average = round(sum(diffs)/len(diffs), 2)
    print("Average change: $" +(str(average)))

#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    months = []
    diffs = []
    #Going over every line
    for line in reader:
      prof_los.append(int(line[1]))
      months.append(line[0])
    
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = prof_los[index] - prof_los[index-1]
        diffs.append(diff)
      except Exception:
        continue
    max = max(diffs)
    min = min(diffs)

    max_index = diffs.index(max) + 1
    min_index = diffs.index(min) + 1

with open('output.txt', 'w') as output_file:
 print("Greatest Increase in Profits: " + months[max_index],max )
 output_file.write('Greatest Increase in Profits: Aug-16 1862002')
 print("Greatest Decrease in Profits: " + months[min_index],min)
 output_file.write('Greatest Decrease in Profits: Feb-14 -1825558')



=======

#Importing Modules
import os 
import csv


# Define Path for the csv files
csvpath = os.path.join("Resources/budget_data.csv")


#Defining the variables and setting up them to zero or a blank list
Total_months = 0 
Net_Profit_loss = []
diff = 0 

# The Start Heading of the statement 
print("Financial Analysis")
print("-------------------------------------------")



#Reading csv
with open (csvpath, newline = "") as csvfile:
    budget_dataCsv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    budgetDatalist = [row for row in budget_dataCsv]          


#print the Total months  
print("Total months :" + str(len(budgetDatalist)))

#Reading csv
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    
    #Going over each line and adding 1 when the Total_months is 0 and then appending to the empty list    
    for line in reader:
        if Total_months==0:
            Total_months+= 1
        Net_Profit_loss.append(int (line[1]))


#printing the Net profit and loss
print("Net profit and loss: $" + str(sum(Net_Profit_loss)))

#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    diffs = []
    #Going over to each lines and append to the prof_los empty list
    for line in reader:
      prof_los.append(int(line[1]))
    #Creating try catch statements 
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = abs(prof_los[index]) - abs(prof_los[index-1])
        diffs.append(diff)
      except Exception:
        continue
        #Finding average and assigning it to a variable then printing
    average = round(sum(diffs)/len(diffs), 2)
    print("Average change: $" +(str(average)))

#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    months = []
    diffs = []
    #Going over every line
    for line in reader:
      prof_los.append(int(line[1]))
      months.append(line[0])
    
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = prof_los[index] - prof_los[index-1]
        diffs.append(diff)
      except Exception:
        continue
    max = max(diffs)
    min = min(diffs)

    max_index = diffs.index(max) + 1
    min_index = diffs.index(min) + 1

with open('output.txt', 'w') as output_file:
 print("Greatest Increase in Profits: " + months[max_index],max )
 output_file.write('Greatest Increase in Profits: Aug-16 1862002')
 print("Greatest Decrease in Profits: " + months[min_index],min)
 output_file.write('Greatest Decrease in Profits: Feb-14 -1825558')



>>>>>>> Stashed changes

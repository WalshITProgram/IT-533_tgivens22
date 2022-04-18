import csv
import json

sales_data = []   # creating blank list 

csv_file = open("SalesJan2022.csv")  #opening file to read

with open("SalesJan2022.csv", "r", newline= '') as csv_file:  #opening csv, setting new start lines
    filtered = (line.replace('\r', '') for line in csv_file)  #creating new iterator, removing \n, cleaning csv 
    csv_reader = csv.reader(csv_file, delimiter=',')          #passing file through reader setting delimiter 
    i = 0                                                     # staring range at 0
    for row in csv_reader:                                    # loop for csv reader, i = 
        print (row)
        i = i +1                                              #creating loop for each record column, it will start at the first record cycle thorugh the next until it reaches ten records
        if(i ==10):
            break





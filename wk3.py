import csv
import json

sales_data = []   # creating blank list 

csv_file = open("SalesJan2022.csv")  #opening file to read

with open("SalesJan2022.csv", "r", newline= '') as csv_file: 
    filtered = (line.replace('\r', '') for line in csv_file)  #creating new iterator, removing \n, cleaning csv 
    csv_reader = csv.reader(csv_file, delimiter=',')          #passing file through reader setting delimiter 





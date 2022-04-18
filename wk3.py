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

#creating dictionaries, adding headers 
first_d = {"Transaction_Date": "1/2/2009 6:17", "Product": "Product 1", "Price": "1200", "Payment_Type": "Mastercard", "Name": "carolina", "City": "Basildon","State": "England", "Country": "United Kingdom"}
second_d = {"Transaction_Date": "1/2/2009, 4:53", "Product": "Product 1", "Price": "1200", "Payment_Type": "Visa", "Name": "Betina", "City": "Parkville", "State":  "MO", "Country":  "United States"}
third_d = {"Transaction_Date": "1/2/2009, 13:08", "Product": "Product 1","Price": "1200", "Payment_Type":"Mastercard", "Name": "Federica e Andrea", "City": "Astoria","State": "OR", "Country": "United States"}
fourth_d = {"Transaction_Date": "1/3/2009, 14:44", "Product": "Product 1", "Price": "1200", "Payment_Type": "Visa", "Name": "Gouya", "City": "Echuca", "State": "Victoria", "Country": "Australia"}
fifth_d = {"Transaction_Date": "1/4/2009, 12:56", "Product": "Product 2", "Price": "3600", "Payment_Type": "Visa", "Name": "Gerd W", "City": "Cahaba Heights", "State": "AL", "Country": "United States"}
sixth_d = {"Transaction_Date": "1/4/2009, 12:56", "Product": "Product 2", "Price": "3600", "Payment_Type": "Visa", "Name": "Gerd W", "City": "Cahaba Heights", "State": "AL", "Country": "United States"}
seventh_d = {"Transaction_Date": "1/4/2009, 20:11", "Product": "Product 1", "Price": "1200", "Payment_Type": "Mastercard", "Name": "Fleur", "City": "Peoria", "State": "IL", "Country": "United States"}
eighth_d = {"Transaction_Date": "1/2/2009, 20:09", "Product": "Product 1", "Price": "1200", "Payment_Type": "Mastercard", "Name": "adam", "City": "Martin", "State": "TN", "Country": "United States"}
ninth_d = {"Transaction_Date": "1/4/2009, 13:17", "Product": "Product 1", "Price": "1200", "Payment_Type": "Mastercard", "Name": "Renee Elisabeth", "City": "Tel Aviv", "State": "Tel Aviv", "Country": "Israel"}

#appending to sales_list
sales_data.append(first_d)
sales_data.append(second_d)
sales_data.append(third_d)
sales_data.append(fourth_d)
sales_data.append(fifth_d)
sales_data.append(sixth_d)
sales_data.append(seventh_d)
sales_data.append(eighth_d)
sales_data.append(ninth_d)

print(sales_data)



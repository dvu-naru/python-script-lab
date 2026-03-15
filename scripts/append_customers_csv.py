import csv

Row = [9600917842, 1, 0, 1, '6040739600-1637823665-468-1637823665@coopmart.vn', 10, '002471318', 0, '2021-11-25 00:01:05', '2022-12-20 21:55:51', 1, 0, '9960407396001', 'NULL', '0739600', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', '6040739600', 'NULL', 'NULL']

file_path = "customers.csv"

with open(file_path, 'a', newline='') as csvFile:
    customer_writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    customer_writer.writerow(Row)

with open(file_path, newline='') as csvFile:
    cust_file = csv.reader(csvFile)

    for row in cust_file:
        print('|'.join(row))


open_file = open("CupcakeInvoices.csv")
value_C = 0
value_V = 0
value_S = 0

open_file = open('CupcakeInvoices.csv')
for line in open_file:
    line = line.split(',')
    for type in line:
        if type == 'Chocolate':
            print('Chocolate')
        elif type =='Strawberry':
            print('Strawberry')
        elif type == 'Vanilla':
            print('Vanilla')

open_file.close()

open_file = open('CupcakeInvoices.csv')
for line in open_file:
    line = line.split(',')
    total = int(line[3]) * float(line[4])
    print("Total:", line[2], '$', round(total))
open_file.close()


import json
import csv
import pandas as pd

newList = []

with open('data.json', 'r')  as file:

    y = json.load(file)
    
    licenseNumber = []

    df_json = pd.read_json('data.json')
    df_json.to_excel('Monthly.xlsx')

    for i in y:
        newList.append(i)
        
        
        # for j in newList:
        #     for c in j: 
        #         licenseNumber.append(c)
        #         print(licenseNumber)
            
with open('daily_test.txt', 'w') as newFile:
    total = 0
    for i in newList:
        total = total + 1
        # input()
    count = 0
    while count < total:
        list1 = newList[count]
        newFile.write("LicenseNo: " + list1['LicenseNo'])
        if 'AcctBal' in list1:
            newFile.write(' Account Balance: ' + str(list1['AcctBal']))
        else:
            newFile.write(' Account Balance: 0')
        
        count = count + 1
        newFile.write('\n')

    submitted_data = y
    monthly_file = open('monthly_file.csv', 'w')

    csv_writer = csv.writer(monthly_file)
    count = 0
    if count == 0:
        header = submitted_data[1].keys()
        csv_writer.writerow(header)
    for i in submitted_data:
        lineData = i.values()
        csv_writer.writerow(lineData)
with open('daily.txt', 'w') as newFile:
    total = 0
    for i in newList:
        total = total + 1
        # input()
    count = 0
    while count < total:
        list1 = newList[count]
        newFile.write(list1['LicenseNo'])
        newFile.write('~')
              
        if 'AcctBal' in list1:
            bal = str(list1['AcctBal'])
            decimal = False
            for i in bal:
                if i == '.':
                    newFile.write(bal)
                    decimal = True
                    # break
                
            if decimal == False:
                newFile.write(bal + '.00')

        else:
            newFile.write('0.00')

        newFile.write('|')

        count = count + 1

        

# with open('data.json') as json_file:
#     data = json.load(json_file)

#     submitted_data = data

#     monthly_file = open('monthly_file.csv', 'w')

#     csv_writer = csv.writer(monthly_file)

#     count = 0

#     for i in submitted_data:
#         if count == 0:
#             header = submitted_data[0].keys()
#             csv_writer.writerow(header)
#             count += 1
#         linedata = submitted_data[i].values()
#         csv_writer.writerow([linedata])

    monthly_file.close()
import json
import csv

newList = []

with open('2021-03-01T07_00_00.000Z_2021-03-12T23_06_48.984Z_e82c0050-2c94-454a-9820-f8027919a570.json', 'r')  as file:

    y = json.load(file)
    
    licenseNumber = []

    for i in y:
        newList.append(i)
        
        
        # for j in newList:
        #     for c in j: 
        #         licenseNumber.append(c)
        #         print(licenseNumber)
            
with open('daily.txt', 'w') as newFile:
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

with open('data.json') as json_file:
    data = json.load(json_file)

    submitted_data = data

    monthly_file = open('monthly_file.csv', 'w')

    csv_writer = csv.writer(monthly_file)

    count = 0

    for i in submitted_data:
        if count == 0:
            header = submitted_data[0].keys()
            csv_writer.writerow(header)
            count += 1
        linedata = submitted_data[i].values()
        csv_writer.writerow([linedata])

    monthly_file.close()
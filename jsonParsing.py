import json
import csv
import pandas as pd

newList = []

with open('data.json', 'r')  as file:

    y = json.load(file)
    
    licenseNumber = []

    # Using Pandas to write the Monthly excel file requested
    df_json = pd.read_json('data.json')
    df_json.to_excel('Monthly.xlsx')

    for i in y:
        newList.append(i)
        
        
# Writing license and account number to test file.  Also writing Monthly test csv file  
with open('daily_test.txt', 'w') as newFile:
    total = 0
    for i in newList:
        total = total + 1
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


# writting daily file in format that is need to upload into css
with open('daily.txt', 'w') as newFile:
    total = 0
    for i in newList:
        total = total + 1
    count = 0
    while count < total:
        list1 = newList[count]
        if 'AcctBal' in list1:
                          
            bal = str(list1['AcctBal'])
            decimal = False
            if bal != "0":

                newFile.write(list1['LicenseNo'])
                newFile.write('~')
                
                for i in bal:
                    if i == '.':
                        newFile.write(bal)
                        decimal = True
                    
                if decimal == False:
                    newFile.write(bal + '.00')


                newFile.write('|')

        count = count + 1

        

    monthly_file.close()
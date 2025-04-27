import csv

cost = 0

with open('data.txt', 'a') as start:
    start.write("Senior member of staff cost:\n")
    start.write("----------------------------\n")
    start.write("ID  staff member     salary\n")
    start.close()
with open('data.csv','a') as startcsv:
    writercsvs = csv.writer(startcsv)
    writercsvs.writerow(["Senior member of staff cost:"])
    writercsvs.writerow(["ID",  "staff member",     "salary"])
with open('personel.csv','r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        if line[5] == 'Senior':
            with open('data.txt', 'a') as fs:
                with open('data.csv', 'a') as ff:
                    writer = csv.writer(ff)
                    # writer.writerow(f"{line[0]} {line[1]:16} ${line[4]}\n")
                    writer.writerow([line[0], line[1], f"${line[4]}"])
                    fs.write(f"{line[0]} {line[1]:16} ${line[4]}\n")
                    cost += int(line[4])
                    fs.close()
            # print(f"{line[0]} {line[1]} {line[4]}")
        # print(line)
        # print(line[0])

with open('data.txt', 'a') as end:
    end.write("----------------------------\n")
    j = f"${cost}"
    end.write(f"Total Cost:          {j}")
    end.close()

with open('data.csv', 'a') as endcsv:
    writercsv = csv.writer(endcsv)
    writercsv.writerow(["----------------------------"])
    writercsv.writerow(['Total Cost:',j])



with open('data.csv', 'r') as filessd:
    reader = csv.DictReader(filessd)
    datas = {row['ID']: row['staff member'] for row in reader}

print(datas['542'])
import csv

cost = 0

with open('data.txt', 'a') as start:
    start.write("Senior member of staff cost:\n")
    start.write("----------------------------\n")
    start.write("ID  staff member     salary\n")
    start.close()
with open('personel.csv','r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        if line[5] == 'Senior':
            with open('data.txt', 'a') as f:
                f.write(f"{line[0]} {line[1]:16} ${line[4]}\n")
                cost += int(line[4])
                f.close()
            # print(f"{line[0]} {line[1]} {line[4]}")

        # print(line)
        # print(line[0])

with open('data.txt', 'a') as start:
    start.write("----------------------------\n")
    j = f"${cost}"
    start.write(f"Total Cost:          {j}")
    start.close()
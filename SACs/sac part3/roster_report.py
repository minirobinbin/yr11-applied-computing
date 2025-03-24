import csv

# team_type = "Men's"
# team_age = "under 20's"
# team_name = "Scorchers"

team_type = input("Team type: ")
team_age = input("Team age: ")
team_name = input("Team name: ")

with open('output.txt','w') as start:
    start.write(f"{team_type} {team_age} {team_name} 2025 ROSTER\n")
    start.write("-------------------\n")
    start.write("Player name     Age Role\n")
    start.write("-------------------\n")


# read the data in from the csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if line[1] == 'Name':
            print()
        else:
            name = line[1]
            age = int(line[4])
            team = line[3]
            role = line[5]
            gender = line[2]
            if team == team_name and 15 < age < 20 and gender == team_type:
                # print(f"{team}{age}")
                with open("output.txt", 'a') as file:
                    file.write(f"{name:16} {age} {role}\n")

                
        
        # print(name)


# create a list of information that the report requires


# create the report text


# write the report to file called {Team Name} {Age Bracket} Roster

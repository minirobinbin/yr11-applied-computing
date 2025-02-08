InputFile = "input.txt"
#print(f'{InputFile}')
OutputFile ='Output.txt'
team1score = 0
team2score = 0

with open(InputFile) as file:
  for line in file:
    line = line.strip().split()
    if "versus" in line:
        # print(f'{line}           team')
        team1 = line[0]
        team2 = line[2]
    if "scored" in line:
        # print(f'{line}            score')
        if f"{team1}" in line:
            team1score = team1score + 1
        if f"{team2}" in line:
            team2score = team2score + 1



    #Append to text file
with open(OutputFile, 'w') as f:
    f.write(f'{team1} scored {team1score} times')
    f.write('\n')
    f.write(f'{team2} scored {team2score} times')
    f.close()

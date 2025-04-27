count = {}

phrase = input("Car: ")

while phrase:
    colours = phrase.split()
    for colour in colours:
        if colour.lower() in count:
            count[colour.lower()] += 1
        else:
            count[colour.lower()] = 1

    phrase = input("Car: ")

for word in count:
    print(f"Cars that are {word}: {count[word]}")

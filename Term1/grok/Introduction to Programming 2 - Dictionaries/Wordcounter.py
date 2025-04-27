count = {}

phrase = input("Enter line: ")

while phrase:
    colours = phrase.split()
    for colour in colours:
        if colour in count:
            count[colour] += 1
        else:
            count[colour] = 1

    phrase = input("Enter line: ")

for word in sorted(count):
    print(f"{word} {count[word]}")

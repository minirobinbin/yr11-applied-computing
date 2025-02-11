lettercount = {}
phrase = input("Enter phrase: ")


while phrase:
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in lettercount:
                lettercount[letter.lower()] +=1
            else:
                lettercount[letter.lower()] = 1

    phrase = input("Eater phrase: ")

letters = sorted(lettercount.keys())

for letter in letters:
    print(letter, lettercount[letter])



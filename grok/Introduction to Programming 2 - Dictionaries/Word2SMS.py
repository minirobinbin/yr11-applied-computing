# A dictionary containing the letter to digit phone keypad mappings.
KEYPAD = {
    'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
    'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
    'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
    'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
    'Z': '9',
}

message = input("Enter word: ")

number = 0
newnumber = []
text = message.upper()
thing = list(text)
#print(f"{thing}")
for test in thing:
    number = number + 1
    joke = KEYPAD[test]
    newnumber.append(joke)

    
joined_number = ''.join(newnumber)
print(f"{joined_number}")


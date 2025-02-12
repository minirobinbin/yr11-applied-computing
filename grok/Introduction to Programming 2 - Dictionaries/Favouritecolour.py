dictionary = {}

namecolour = input('Name and colour: ')
while namecolour:
  name, colour = namecolour.split()
  dictionary[name] = colour
  namecolour = input('Name and colour: ')


for name, colour in dictionary.items():
    print(f'{name} {colour}')
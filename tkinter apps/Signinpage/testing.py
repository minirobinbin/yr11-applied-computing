characters = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")"}
upperletters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
lowerletters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
determine = input("what")




has_uppercase = any(char.isupper() for char in determine) 
has_lowercase = any(char.islower() for char in determine) 
has_special = any(not char.isalnum() for char in determine)  

if has_uppercase and has_lowercase and has_special:
    print("yes")
    
# for letter in determine:
#     if letter in characters:  
#         if letter in upperletters: 
#             if letter in lowerletters:
#                 print("there is everything")
#             else:
#                 print("no lowerletters")
#         else:
#             print("no upperletters")
#     else:
#         print("no character")
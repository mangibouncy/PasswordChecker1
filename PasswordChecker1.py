import re
#create a program that takes input from user and checks if password is good or bad
#it's good if it has at least 1 uppercase letter, 8 or more characters, at least 1 number and one special character

user = input("Enter passowrd: ")

hasNumber = False
hasUppercase = False
hasSpecial = False

if len(user) < 8:
    print("WEAK PASSWORD")
    exit()
else:
    for letter in user:
        if letter.isupper():
            hasUppercase = True

    for letter in user:
        if letter.isdigit():
            hasNumber = True

    if re.search(r'[^a-zA-Z0-9]', user): #the re class can help pick out special characters
                                            # a-z is the lowercase alphabet; A-Z is the uppercase; 0-9 is the number range; ^ means anything not in there
            hasSpecial = True

if hasNumber and hasSpecial and hasUppercase:
    print ("GOOD PASSWORD")
else:
    print("WEAK PASSWORD")

#password_strenght

import re

def  password_level(password):

    level_0 = r"^\S{8,}$"
    level_1 = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    level_2 = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    level_3 = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    #Strengh level variable
    strength_level = 0

    if re.match(level_0, password):
        strength_level = 0
    if re.match(level_1, password):
        strength_level = 1
    if re.match(level_2, password):
        strength_level = 2
    if re.match(level_3, password):
        strength_level = 3

    if strength_level == 0:
        print("\nPassword strenght level: 0 ")

    elif strength_level == 1:
        print("\nPassword strenght level: 1 ")

    elif strength_level == 2:
        print("\nPassword strenght level: 2 ")

    elif strength_level == 3:
        print("\nPassword strenght level: 3 ")

    else:
        print("\nInvalid password format.")

#Input from the user

print("\nPASSWORD STRENGHT: \nLevel 0: eight characters that are not spaces. \nLevel 1: eight characters with at least one letter and one number. \nLevel 2: level 1 and one special character (@$!%*#?&). \nLevel 3: level 2 and one upper case character. ")

password = input("\nEnter password: ")
password_level(password)


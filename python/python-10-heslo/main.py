import hashlib

def contains_special(passin):
    specials = "!?@#$%_-"
    for x in specials:
        if x in passin:
            return 1
    return 0

def contains_chars_and_nums(passin):
    uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    safety = 0
    for x in uppercaseLetter:
        if x in passin:
            safety += 1
            break
    for x in uppercaseLetter.lower():
        if x in passin:
            safety += 1
            break
    for x in numbers:
        if x in passin:
            safety += 1
            break
    return safety

def contains_common(passin):
    commonPassword = ["qwertzui", "qwertyui", "abcdefgh", "password", "password123", "12345678"]
    for x in commonPassword:
        if x in passin.lower():
            return 0
    return 1

def check_safety(passin):
    return contains_special(passin) + contains_chars_and_nums(passin) + contains_common(passin)

storedPasswords = []
def check_similarity(passin):
    global storedPasswords
    hashedPassin = hashlib.sha256(passin.encode()).hexdigest()
    print(hashedPassin)
    for x in storedPasswords:
        if hashedPassin == x:
            return 1
    storedPasswords.append(hashedPassin)
    return 0

while(True):
    password = input("password: ")
    if len(password) >= 8:
        print(f"Your password is this safe: {check_safety(password)}/5")

        if check_similarity(password):
            print("your password matches with another one (not saved)")
        else:
            print("your password matches with neither of your passwords (saved hash)\n")
        if input("Store a new password? [y/n]: ").upper() == 'n'.upper():
            break
    else:
        print("Password length must be atleast 8 characters long.")
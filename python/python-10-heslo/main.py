import hashlib

uppercaseLetter = "ABCDEFGHIJKLMNOPQRST"
password = input("password: ")
passwords = ["a"]

def contains_special(passin):
    if '!' in passin or '@' in passin or '#' in passin or '$' in passin or '%' in passin or '_' in passin or '-' in passin:
        return 1
    return 0

def contains_uppercase(passin):
    for x in uppercaseLetter:
        if x in passin:
            return 1
    return 0

def check_safety(passin):
    safetyMeter = 0
    if len(passin) >= 8:
        safetyMeter += 1
    if contains_special(passin):
        safetyMeter += 1
    if contains_uppercase(passin):
        safetyMeter += 1
    return safetyMeter

def check_similarity(passin):
    hashed = hashlib.new('sha256')
    passin = hashed.update(passin.encode())
    if passin in passwords:
        return 1
    passwords += passin
    return 0

print(f"Your password is this safe: {check_safety(password)}/3")

if check_similarity(password):
    print("your password matches with another one")
else:
    print("your password matches with neither of your passwords (saved hash)")
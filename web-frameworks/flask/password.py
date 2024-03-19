import hashlib

def contains_special(passin):
    if '!' in passin or '@' in passin or '#' in passin or '$' in passin or '%' in passin or '_' in passin or '-' in passin:
        return 1
    return 0

def contains_uppercase(passin):
    uppercaseLetter = "ABCDEFGHIJKLMNOPQRST"
    for x in uppercaseLetter:
        if x in passin:
            return 1
    return 0

def contains_common(passin):
    commonPassword = ["qwertzui", "qwertyui", "abcdefgh", "password", "password123", "12345678"]
    for x in commonPassword:
        if x in passin.lower():
            return 1
    return 0

def check_safety(passin):
    safetyMeter = 0
    if contains_special(passin):
        safetyMeter += 1
    if contains_uppercase(passin):
        safetyMeter += 1
    if not contains_common(passin):
        safetyMeter += 1
    return safetyMeter

storedPasswords = []
def check_similarity(passin):
    global storedPasswords
    # hashedPassin = hashlib.sha256(passin.encode()).hexdigest()
    hashedPassin = passin
    print(hashedPassin)
    for x in storedPasswords:
        if hashedPassin == x:
            return 1
    storedPasswords.append(hashedPassin)
    return 0
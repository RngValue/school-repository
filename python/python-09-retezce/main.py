fname = "  Duolingo"
lname = "Owl  "
name = fname + " " + lname

print("upper():\t" + name.upper())
print("lower():\t" + name.lower())
print("count('o'):\t" + str(name.count('o')))
print("index('o'):\t" + str(name.index('o')))
print("index('o', 5):\t" + str(name.index('o', 5)))
print("lstrip():\t" + name.lstrip())
print("rstrip():\t" + name.rstrip())
print("strip():\t" + name.strip())
print("replace('o', ' uwu '):\t" + name.replace('o', ' uwu '))
print("startswith('D'):\t" + str(name.startswith('D')))
print("endswith('n'):\t" + str(name.endswith('n')))
print("format():\t" + "Say it with me! {0}".format(name))
print("multiplication:\t" + name * 5)
print("len():\t" + str(len(name)))
print("in:\t" + 'o' in name)
print("not in:\t" + 'o' not in name)
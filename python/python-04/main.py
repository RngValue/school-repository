#name_bruh = input("My name is... ")
#print(f"🐸 I'm {name_bruh} bruh 🐸")
#print(f"😊 I am {len(name_bruh)} years old 😊")

#number = 3

#if number > 5:
#  print(f"Numbah {number} be on top more than 5 fr")
#else:
#  print(f"Numbah {number} be on top less than 5 fr")

#1. Uživatel může zadávat vstupní hodnoty a operace.
x = float(input("first number: "))
y = float(input("second number: "))
operation = input("[+/-/*//]: ")

result = 0
modulo = 0
if operation == '-':
  result = x - y
elif operation == '*':
  result = x * y
elif operation == '/':
  result = x / y
  modulo = x % y
else:
  result = x + y

print(f"result:\t\t\t\t{result}")
if operation == '/':
  print(f"modulo:\t\t\t\t{modulo}")
print("\n")

#Cykly
#1. Vypište všechna čísla od 1 do 10 pomocí cyklu for.
for i in range(0, 10):
  print(f"for 1-10:\t\t\t{i+1}")
print("\n")

#2. Vypište všechna sudá čísla od 2 do 10 pomocí cyklu while.
j = 2
while (j <= 10):
  if j % 2 == 0:
    print(f"while sudá 2-10:\t{j}")
  j += 1
print("\n")

#3. Udělejte součet čísel od 1 do 10 pomocí cyklu for.
result = 0
for i in range(0, 10):
  result += i + 1
print(f"for součet:\t\t\t{result}")

#4. Udělejte součin čísel od 1 do 5 pomocí cyklu while.
j = 1
result = 1
while (j <= 5):
  result *= j
  j += 1
print(f"while součin:\t\t{result}")

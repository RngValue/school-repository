def bubble_sort(pole):
  swapped = False
  delkaPole = len(pole)
  for i in range(delkaPole-1):
    for j in range(0, delkaPole-i-1):
      if pole[j] > pole[j+1]:
        swapped = True
        pole[j], pole[j+1] = pole[j+1], pole[j]
    if not swapped:
      return

pole = [5, 3, 4, 7, 8, 6, 9, 0, 1, 2]

print(f"Pole = {pole}")

#Funkce sorted()
print(f"Python funkce sorted() => {sorted(pole)}")

#Bubble sort
bubble_sort(pole)
print(f"Bubble sort => {pole}")
def bubble_sort(pole):
  swapped = False
  delkaPole = len(pole)
  for i in range(delkaPole - 1):
    for j in range(delkaPole - i - 1):
      if pole[j] > pole[j + 1]:
        swapped = True
        pole[j], pole[j + 1] = pole[j + 1], pole[j]
    if not swapped:
      return


def select_sort(pole):
  delkaPole = len(pole)
  for i in range(delkaPole):
    minI = i
    for j in range(i + 1, delkaPole):
      if pole[j] < pole[minI]:
        minI = j
    (pole[i], pole[minI]) = (pole[minI], pole[i])


def insert_sort(pole):
  delkaPole = len(pole)
  for i in range(1, delkaPole):
    current = pole[i]
    j = i - 1
    while j >= 0 and current < pole[j]:
      pole[j + 1] = pole[j]
      j -= 1
    pole[j + 1] = current


pole = [5, 3, 6, 1, 4, 2]
print(f"Neseřazené pole:\t{pole}")
bubble_sort(pole)
print(f"Bubble sort:\t\t{pole}")

pole = [5, 3, 6, 1, 4, 2]
select_sort(pole)
print(f"Select sort:\t\t{pole}")

pole = [5, 3, 6, 1, 4, 2]
insert_sort(pole)
print(f"Insert sort:\t\t{pole}")

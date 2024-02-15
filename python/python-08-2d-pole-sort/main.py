def bubble_sort(unsortedArray):
  arrayLength = len(unsortedArray)
  for k in range(arrayLength):
    for i in range(len(unsortedArray[k]) - 1):
      for j in range(len(unsortedArray[k]) - i - 1):
        if unsortedArray[k][j] > unsortedArray[k][j + 1]:
          unsortedArray[k][j], unsortedArray[k][j + 1] = unsortedArray[k][j + 1], unsortedArray[k][j]
  return unsortedArray

def select_sort(unsortedArray):
  arrayLength = len(unsortedArray)
  for k in range(arrayLength):
    for i in range(len(unsortedArray[k])):
      minI = i
      for j in range(i + 1, len(unsortedArray[k])):
        if unsortedArray[k][j] < unsortedArray[k][minI]:
          minI = j
      unsortedArray[k][i], unsortedArray[k][minI] = unsortedArray[k][minI], unsortedArray[k][i]
  return unsortedArray


def insert_sort(unsortedArray):
  arrayLength = len(unsortedArray)
  for k in range(arrayLength):
    for i in range(1, len(unsortedArray[k])):
      current = unsortedArray[k][i]
      j = i - 1
      while j >= 0 and current < unsortedArray[k][j]:
        unsortedArray[k][j + 1] = unsortedArray[k][j]
        j -= 1
      unsortedArray[k][j + 1] = current
  return unsortedArray

def print_2d_maxtrix(v: list[list[int]]):
  for i in range(len(v)):
    print(v[i])

print("The unsorted 2D array:")
print_2d_maxtrix([[5,8,6], [8,2,5], [0,2,1]])

print("\nBubble sort:")
arr = [[5,8,6], [8,2,5], [0,2,1]]
print_2d_maxtrix(bubble_sort(arr))

print("\nSelect sort:")
arr = [[5,8,6], [8,2,5], [0,2,1]]
print_2d_maxtrix(select_sort(arr))

print("\nInsert sort:")
arr = [[5,8,6], [8,2,5], [0,2,1]]
print_2d_maxtrix(insert_sort(arr))
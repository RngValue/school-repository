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

def partition(unsortedArray, low, high):
    pivot = unsortedArray[high]
    i = low - 1
    for j in range(low, high):
        if unsortedArray[j] <= pivot:
            i = i + 1
            (unsortedArray[i], unsortedArray[j]) = (unsortedArray[j], unsortedArray[i])
    (unsortedArray[i + 1], unsortedArray[high]) = (unsortedArray[high], unsortedArray[i + 1])
    return i + 1
 
def quick_sort(unsortedArray, low, high):
  if low < high:
    part = partition(unsortedArray, low, high)
    quick_sort(unsortedArray, low, part - 1)
    quick_sort(unsortedArray, part + 1, high)

def quick_sort_2d(unsortedArray):
  for i in range (len(unsortedArray)):
    low = 0
    high = len(unsortedArray[i])
    quick_sort(unsortedArray[i], low, high - 1)

def print_2d_maxtrix(v):
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

print("\nQuick sort:")
arr = [[5,8,6], [8,2,5], [0,2,1]]
quick_sort_2d(arr)
print_2d_maxtrix(arr)
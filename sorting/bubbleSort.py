def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

def bubble_sort_unoptimized(arr):
  for el in arr:
    for index in range(len(arr) - 1):
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)


def bubble_sort_optimized(arr):
  for i in range(len(arr)):
    for idx in range(len(arr) - i - 1):
      if arr[idx] > arr[idx + 1]:
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
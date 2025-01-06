import random

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

random_list = [random.randint(0, 100) for _ in range(10)]
print("Original list:", random_list)

insertion_sort(random_list)
print("Sorted list:", random_list)
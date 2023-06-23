def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

array = [4, 2, 7, 1, 9, 5]
sorted_array = selection_sort_descending(array)
print(sorted_array)

def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

my_list = [5, 2, 8, 1, 9, 3]
sorted_list = bubble_sort_descending(my_list)
print(sorted_list)

def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

array = [4, 2, 7, 1, 9, 5]
sorted_array = insertion_sort_descending(array)
print(sorted_array)

def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_descending(arr[:mid])
    right = merge_sort_descending(arr[mid:])

    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [9, 5, 7, 2, 4, 1, 8, 3, 6]
sorted_arr = merge_sort_descending(arr)
print(sorted_arr)

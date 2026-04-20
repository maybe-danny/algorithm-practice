def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def gnomeSort(arr, n):
    ind = 0
    while ind < n:
        if ind == 0:
            ind += 1
        if arr[ind] >= arr[ind - 1]:
            ind += 1
        else:
            arr[ind], arr[ind - 1] = arr[ind - 1], arr[ind]
            ind -= 1
    return arr

def bubble_sort(arr: list) -> list:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
    return arr

if __name__ == '__main__':
    # Example
    print(bubble_sort([4, 8, 6, 71, 52, 51, 11, 73, 2, 62, 88, 29, 5, 61, 31, 40, 30, 94, 89, 100]))

def selection(arr: list) -> list:
    for i in range(len(arr)):
        min_index = i
        for k in range(i, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    # Example
    print(selection([6,4,8,2,4,9]))
    print(selection([23, 61, 55, 31, 12, 39, 40, 56, 72, 18, 4, 54, 30, 76, 20, 96, 77, 48, 70, 13]))
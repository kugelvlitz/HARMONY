def insertion(arr: list) -> list:
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for k in range(i, 0, -1):
                if arr[k] < arr[k-1]:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
    return arr


if __name__ == '__main__':
    # Example
    print(insertion([6,4,8,2,4,9]))
    print(insertion([23, 61, 55, 31, 12, 39, 40, 56, 72, 18, 4, 54, 30, 76, 20, 96, 77, 48, 70, 13]))
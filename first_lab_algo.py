def is_monotone(arr):
    def increasing():
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def descending():
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
        return True

    return increasing() or descending()
print(is_monotone([2, 2, 2, 2, 2]))   
print(is_monotone([2, 2, 2, 2, 1]))   
print(is_monotone([2, 2, 2, 2, 3]))   

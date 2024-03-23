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
print(is_monotone([1,2,3,4,4,5]))   

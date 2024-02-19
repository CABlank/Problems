print("Hello, World!")

arr = [1, 2, 3, 2, 3, 5, 1]

def myFunction(arr):
    # Initialize result array with 1s
    result = [1] * len(arr)

    for index in range(len(arr)):
        # Boundary checks for the first and last elements
        if index == 0:
            if arr[index] <= arr[index + 1]:
                result[index] = 1
            else:
                result[index] = 2
        elif index == len(arr) - 1:
            if arr[index] <= arr[index - 1]:
                result[index] = 1
            else:
                result[index] = 2
        else:
            # For elements not at the boundaries
            if arr[index] <= arr[index + 1] and arr[index] <= arr[index - 1]:
                result[index] = 1
            elif (arr[index] > arr[index + 1] and arr[index] <= arr[index - 1]) or \
                 (arr[index] <= arr[index + 1] and arr[index] > arr[index - 1]):
                result[index] = 2
            elif arr[index] > arr[index + 1] and arr[index] > arr[index - 1]:
                result[index] = 3

    print(result)
myFunction(arr)

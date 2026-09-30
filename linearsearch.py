def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Not found


numbers = [10, 25, 7, 40, 15]
target = 40

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

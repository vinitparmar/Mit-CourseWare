def insertionSort(arr):
    # travese through 1 to len of array
    for i in range(1,len(arr)):
        key = arr[i]

        j= i-1

        while key < arr[j] and j >= 0:
            # shifting the numbers in array
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key


# drivers code
arr = [12,11,13,5,6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

# Time Complexity: O(n*2)

# Auxiliary Space: O(1)
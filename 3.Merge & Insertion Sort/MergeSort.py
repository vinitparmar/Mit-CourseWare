def mergeSort(arr):
    if len(arr) > 1:

        # find the element
        mid  =  int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        # sorting the left half
        mergeSort(left)
        # sorting the right half
        mergeSort(right)

        i = j = k = 0

        # copy the array in temp array left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i=i+1
            else:
                arr[k] = right[j]
                j=j+1

            k=k+1

        # checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            k=k+1
            i=i+1
        while j < len(right):
            arr[k] = right[j]
            j=j+1
            k=k+1

# drivers code
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
if len(arr) > 1:
    for i in range(len(arr)):
        print("% d" % arr[i])
else:
    print("array is empty")
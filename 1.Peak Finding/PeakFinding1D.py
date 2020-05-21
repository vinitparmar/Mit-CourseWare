#peak finder algo for 1 Dimenional Array

def peakFinderUtil(arr,leftPtr,rightPtr,arr_length):
    
    #find the mid element
    mid = leftPtr +(rightPtr-leftPtr)/2
    #number are passsed as string in python parameter
    #convert to string
    mid = int(mid)

    #compare the mid element if neighbours exist
    #it also acts as base condition
    if((mid == leftPtr or arr[mid-1]<=arr[mid]) and 
    (mid == rightPtr or arr[mid] >= arr[mid+1])):
        return mid

    # if middle element is not the peak
    # left element is greater than mid
    # then traverse the left half
    elif(mid > 0 and arr[mid] <= arr[mid-1]):
        return peakFinderUtil(arr,leftPtr,mid-1,arr_length)

    # if middle element is not the peak
    # right element is greater than mid
    # then traverse the right half
    else:
        return peakFinderUtil(arr,mid+1,rightPtr,arr_length)


def peakFinder(arr,n):
    return peakFinderUtil(arr,0,n-1,n)

#Driver code
# parameter to be passed is:
# 1.Array
# 2.length of the array
arr = [1, 3, 20, 4, 1, 0] 
length = len(arr)
# we will be returning the index of the peek  
print(arr)
print("the index of the peak is : ",peakFinder(arr,length))
print("peak element is : ",arr[peakFinder(arr,length)])

# Complexity analysis

# Time complexity:
# for each search operation the iteration becomes half
# so complexity becomes O(Log n)

# Space compelcty:
# no extra space is required
# so complexity becomes O(1)

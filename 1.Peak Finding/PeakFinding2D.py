

from math import ceil

def findPeakRec(arr,rows,cols,mid):
    max = 0
    # evaluating the max of mid column
    max,max_index = find_max(arr,rows,mid,max)

    # if we are o the 1st and last column
    # max is the peak
    if(mid == 0 or mid == cols-1):
        return max


    #  If max is less than its left 
    if(max >= arr[max_index][mid-1] and max >= arr[max_index][mid+1]):
        return max


    #  If max is less than its left 
    if(max < arr[max_index][mid-1]):
        return findPeakRec(arr,rows,cols,mid-ceil(mid/2.0))

    
    #if(max < arr[max_index][mid+1]):
    #  If max is less than its right 
    return findPeakRec(arr,rows,cols,mid+ceil(mid/2.0))

# function to find max in column
def find_max(arr,rows,mid,max):
    max_index = 0
    for i in range(rows):
        if(max < arr[i][mid]):
            max = arr[i][mid]
            max_index = i
    
    return max,max_index



def findPeak(arr,rows,cols):
    return findPeakRec(arr,rows,cols,cols//2)



# Driver Code 
arr = [ [ 10, 8, 10, 10 ], 
        [ 14, 13, 12, 11 ], 
        [ 15, 9, 11, 21 ], 
        [ 16, 17, 19, 20 ] ] 
  
# Number of Columns 
rows = 4
columns = 4
print(arr)
print("Peak in 2D Array is : ",findPeak(arr, rows, columns)) 

# Time Complexity : O(rows * log(columns)
# Auxiliary Space: O(columns/2) 
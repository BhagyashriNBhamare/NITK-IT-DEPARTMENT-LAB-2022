def mergeSort(arr, n,b): 

    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1,b) 


def _mergeSort(arr, temp_arr, left, right,b): 



    inv_count = 0


    if left < right: 

        mid = left+(right-left)//2



        inv_count += _mergeSort(arr, temp_arr, left, mid,b) 



        inv_count += _mergeSort(arr, temp_arr, mid + 1, right,b) 



        inv_count += merge(arr, temp_arr, left, mid, right,b) 
    return inv_count 


def merge(arr, temp_arr, left, mid, right,b): 
    i = left  
    j = mid + 1 
    k = left    
    inv_count = 0


    while i <= mid and j <= right: 

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else:
            if arr[i] > arr[j]*b:
                inv_count += (mid-i + 1)
            temp_arr[k] = arr[j]  
            k += 1
            j += 1

    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1


    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1

    # Copy the sorted subarray into Original array 
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
    # print(left,mid,right,inv_count )     
    return inv_count 

s=raw_input("Entre The Array ")
arr=list(map(int,s.split(" ")))
w=list(map(int,s.split(" ")))
m=raw_input("Entre The value of b ")
m=int(m)
b=m
n = len(arr) 

result = mergeSort(arr, n,b) 
# if w[0]>w[n-1]*b:
#     result=result+1
print("Number of inversions are", result) 
      


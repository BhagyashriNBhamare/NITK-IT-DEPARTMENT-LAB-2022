import sys

def countBinversions(arr,b,n,w):

    result = mergeSort(arr,n,b) 
    if w[0]>w[n-1]*b and n!=2:
        result=result+1
    print("Number of inversions are", result) 
def mergeSort(arr, n,b): 

    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1,b) 


def _mergeSort(arr, temp_arr, left, right,b): 



    inv_count = 0


    if left < right: 

        mid = (left+right)//2



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
            if  arr[i] <= arr[j]*b:
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

    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 

def main():
    
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1] 
    file=open(fname,'r')
    
    numTestcases = int(file.readline())

    for i in range(numTestcases):
        line = file.readline() # Read in the numbers in the sequence

        # Print the numbers in the sequence one by one.
        s=[]
        e=[]
        for w in line.split(' '):
    	    print(w),
            s.append(int(w))
            e.append(int(w))
        b = file.readline() # The number b
        p=int(b)
        print(b) 
        countBinversions(s,p,len(s),e)

    file.close()

if __name__ == '__main__':
    main()
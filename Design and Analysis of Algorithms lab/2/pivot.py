def main(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        m=l+(r-l)//2
        if m==0 or m==len(arr)-1:
            return m
        elif arr[m-1]<arr[m] and arr[m+1]<arr[m]:
            return m
        elif arr[m]<arr[m-1] and m>0:
            r=m-1
        else:
            l=m+1
s=raw_input("entre the array ")
a=list(map(int,s.split(" ")))
print("pivot element at index "+str(main(a)))





import sys
import collections

def solve( A):

    if len(A)==1:
            return 0
    p={}
    sum=0
    nums=[]
    for x in A:
        nums.append(x)
    for x in nums:
        sum=sum+x
    w=sum
    total=sum
    sum=(sum//2)
    dp=[[0 for x in range(sum+1)]for y in range(len(nums)+1)]
    nums.sort()
    dp[0][0]=0
    for x in range(1,len(nums)+1):
        dp[x][0]=0
        for y in range(1,sum+1):
            if dp[x-1][y]>0 and y-nums[x-1]>=0:
                if y-nums[x-1]==0:
                    dp[x][y]=1
                elif dp[x-1][y-nums[x-1]]!=0:
                    dp[x][y]=min(dp[x-1][y],1+dp[x-1][y-nums[x-1]])
                else:
                    dp[x][y]=dp[x-1][y]
            elif dp[x-1][y]==0 and y-nums[x-1]>=0:
                if y-nums[x-1]==0:
                    dp[x][y]=1
                elif dp[x-1][y-nums[x-1]]!=0:
                    dp[x][y]=1+dp[x-1][y-nums[x-1]]
                else:
                    dp[x][y]=dp[x-1][y]
            else:
                dp[x][y]=dp[x-1][y]
    x=len(nums)
    y=sum

    while y>=0 :
        print(y,dp[x][y])
        if dp[x][y]>0  and abs((len(nums)-dp[x][y])-dp[x][y])<=1  :
            break
        y=y-1
    q=[]
    q.append(y)
    q.append(total-y)
    q.sort()
    for x in q:
        print(x),
    # print(y,total-y)


def main():
    
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1] 
    file=open(fname,'r')
    
    numTestcases = int(file.readline())
    s=[]
    for i in range(numTestcases):
        line = file.readline() # Read in the numbers in the sequence

        # Print the numbers in the sequence one by one.
        w=int(line)
        s.append(w)
        # b = file.readline() # The number b
        print(w) 


    file.close()
    solve(s)

if __name__ == '__main__':
    main()

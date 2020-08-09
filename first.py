import  sys
n=int(input("Enter number of books "))
y=int(input("Enter number of students "))
arr=[]
print("Enter pages in book :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

arr.sort()
sum=0
for i in range(0,n):
        sum=sum+arr[i]

def check(mid):
    students_allocated=1
    pages=0
    for i in range(0,n):
            if(arr[i]>mid):
                return False
            if (pages+arr[i]>mid):
                students_allocated=students_allocated+1
                pages=arr[i]
                if (students_allocated > y):
                    return False
            else:
                pages=pages+arr[i]
    return True


def binarySearch():
    if (n < y):
      return -1
    lower=arr[n-1]
    upper=sum
    min=sys.maxsize
    while lower <= upper: 
  
        mid = lower + ( (upper-lower) // 2); 
        if (check(mid)): 
            if(mid<min):
                min=mid
            upper=mid-1
        else: 
            lower=mid+1
    return min

p=binarySearch()
if (p==-1):
    print("Not Possible")
else:
    print("Minimum number of pages which should be assigned to student ",p)

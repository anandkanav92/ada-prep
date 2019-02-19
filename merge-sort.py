import math

n=[4,5,2,-5,2,7,1]
def mergesort(n,left,right):
  #print_custom(n,left,right)
  if left==right:
    return
  mid = math.floor((left+right)/2)
  mergesort(n,left,mid)
  mergesort(n,mid+1,right)
  merge(n,left,mid,right)
  print("call merge here %d,%d,%d",left,mid,right)

def print_custom(n,left,right):
  print("printing the array")
  while left<=right:
    print(n[left])
    left+=1

def merge(n,left,mid,right):
  # Iterate through all
  # elements of ar2[] starting from
  # the last element
  left_index=left
  right_index=right
  while right_index>=mid+1:
    last = n[mid]
    mid_index=mid-1
    while mid_index>=left and mid_index>=0 and n[right_index]<n[mid_index]:
      n[mid_index+1] = n[mid_index]
      mid_index-=1

    if (mid_index != mid-1 or last > n[right_indexlsgit ]):
      n[mid_index+1]=n[right_index]
      n[right_index]=last

    right_index-=1
  print(n)



mergesort(n,0,6)
print(n)

import math
#contain all the major sorts


n=[4,5,2,-5,2,7,1]
def merge_sort(n,left,right):
  #print_custom(n,left,right)
  if left==right:
    return
  mid = math.floor((left+right)/2)
  merge_sort(n,left,mid)
  merge_sort(n,mid+1,right)
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

def quick_sort(n,left,right):
  if left==right:
    return
  else:
    index=partition_qs(n,left,right)
    print(index)
    quick_sort(n,left,index-1)
    quick_sort(n,index+1,right)


def partition_qs(n,left,right):
  #choosing last element as pivot
  i = ( left-1 )         # index of smaller element
  pivot = n[right]     # pivot
  for j in range(left , right):

    # If current element is smaller than or
    # equal to pivot
    if   n[j] <= pivot:

      # increment index of smaller element
      i = i+1
      n[i],n[j] = n[j],n[i]

  n[i+1],n[right] = n[right],n[i+1]
  return ( i+1 )

def heapify(n,length,index):
  largest = index
  left = 2*index+1
  right = 2*index+2

  if left < length and n[left]>n[largest]:
    largest=left

  if right < length and n[right]>n[largest]:
    largest=right

  if index!=largest:
    n[largest],n[index]=n[index],n[largest]
    heapify(n,length,largest)

def heap_sort(n,length):
  temp = length//2-1
  while temp>=0:
    heapify(n,length,temp)
    temp = temp//2-1

  for i in range(length-1,-1,-1):
    n[i],n[0]=n[0],n[i]
    heapify(n,i,0)

heap_sort(n,7)
print(n)
#quick_sort(n,0,6)
#merge_sort(n,0,6)
#print(n)

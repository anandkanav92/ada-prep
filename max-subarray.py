# noob way is to check all the possible subsets using 3 loops. First for starting point and second for end point and one to loop in the middle

# improvement is eliminating the middle loop by summing over the elements between starting and ending loop

# best is below.O(n) It check the sum at every element, check if the element is greater than the prior subarray added with sum.
n=[2,-2,-1,2,4,-3,5,2,-5,2]
sum_inter = 0
best = 0
print(n)
for i in n:
  sum_inter = max(i,i+sum_inter)
  best = max(best,sum_inter)
  print('sum is ',sum_inter, 'and best is',best)
print(best)

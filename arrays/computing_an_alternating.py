# Computing an alternation - process of rearranging an array so that elements
# alternate in some patten. 
# high-low-high-low

"""
PROBLEM: Write a program that takes an array A of n numbers, and rearranges A's
elements to get a new array B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5]

Hint: Can you solve the problem by making local changes to A?
"""

# Two options: could simply rearrange the elements around the median, and then
# then perform the interleaving. time complexity of 0(n)
# OR we could simply iterare through the array and swapping A[i] and A[i + 1] 
# when i is even and A[i] > A[i + 1] or i is odd and A[i] < A[i + 1] achieves
# the desired configuration

#def rearrange(A):
#    for i in range(len(A)):
#        A[i:i+2] = sorted(A[i:i+2], reverse=i % 2)
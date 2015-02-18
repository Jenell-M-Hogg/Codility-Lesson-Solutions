'''A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
Write a function:
def solution(A)
that, given a zero-indexed array A, returns the value of the missing element.
For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
Assume that:
N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.'''

#100% solution


def solution(A):

    #None of the integers repeat...I'll just use the built in sort!
    A.sort()
    #Python is so fucking nice.

    
    #Check to see if the list is empty
    n=len(A)
    if n==0:
        return 1
    
    #Now, I just need to find the missing integer... It could be the first element thats missing, soo...
    
    if A[0]!=1:
        return 1

    #It could be the last element missing!

    if A[n-1]!=n+1:
        return n+1

    #Otherwise, search for the hole!
    n=len(A)
    if n==0:
        return 1

    for i in range(n-1):
        #I already validated A[0]. Now I have to check the next element.
        #If the next element is NOT the integer after the previous, then that is the missing element 

        if A[i+1]!=A[i]+1:
            return A[i]+1

    
    pass




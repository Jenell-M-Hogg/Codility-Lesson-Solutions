'''A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
def solution(A)
that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
Assume that:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified'''

def solution(A):
    #It is assumed that N is of size 1 atleast.
    #Use the built in sorting method
    A.sort()

    #I'm paranoid so I'll check the length of the list regardless
    n=len(A)
    if n==0:
        return 0

    #If the first element isn't 1, get rid of it
    if A[0]!=1:
        return 0

    #If the last element isn't the size of the array, get rid of it!
    if A[n-1]!=n:
        return 0

    #The first and last element has been verified. Now, starting from both ends, verify there are no "holes"

    for i in range(1,n-1):
        backindex=n-i-1

        f=A[i]
        l=A[i-1]

        bf=A[backindex]
        bl=A[backindex+1]

        if f!=l+1:
            return 0

        if bf!=bl-1:
            return 0

    return 1
    pass

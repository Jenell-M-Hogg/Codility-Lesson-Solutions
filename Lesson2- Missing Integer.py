'''Write a function:
def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer that does not occur in A.
For example, given:
  A[0] = 1    
  A[1] = 3    
  A[2] = 6
  A[3] = 4    
  A[4] = 1    
  A[5] = 2
the function should return 5.

Assume that:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.'''

#100% Solution

def solution(A):
    A.sort()
    ind=findPosIndex(A)

    #If A is filled with negatives, just return 1
    if ind==-1:
        return 1

    #A has atleast one positive value.
    #The lowest value may occur before the first positive value in A

    if A[ind]!=1:
        return 1

    #The first positive value may be 1! then, we need to search for a "hole",
    #starting with the least positive values and then going up.

    for i in range(ind+1,len(A)):
        #If there's a hole, return the hole... Worst case this gets to the end and returns the next value
        nex=A[i]
        shouldne=A[i-1]+1
        
        if nex!=A[i-1]:
            if nex!=shouldne:
                return shouldne


    return A[len(A)-1]+1
            

    
    
    pass


def findPosIndex(A):
    #Findsthe index of the first positive integer in A. If there is no
    # positive integers, returns -1

    n=len(A)

    for i in range(n):
        if A[i]>0:
            return i

    return -1

solution([1, 2,3,4,5,5])

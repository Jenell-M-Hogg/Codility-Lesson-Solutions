'''A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X. Leaves fall from a tree onto the surface of the river.
You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in minutes.
The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X.
For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In minute 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
Write a function:
def solution(X, A)
that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
If the frog is never able to jump to the other side of the river, the function should return −1.
For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above. Assume that:
N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.'''


#THIS ANSWER IS FUNCTIONAL, BUT NOT OPTIMIZED
# 72% answer

# I suspect the X in A, and -1 in p to be the culprit.

def solution(X, A):
    # We know right away if the last leaf doesn't fall the frog will never get there
    if False==(X in A):
        return -1

    #We know right away that if A is not as long as X is there is no way the frog will ever reach there!
    if len(A)<X:
        return -1
    
    p=[]
    for i in range(X):
        p.append(-1)

    #Fill the array p with X -1. This array will be filled with the minutes at which each position is covered by a leaf. If its left as -1, then no leaf is ever placed

    n=len(A)
    for i in range(n):
        position=A[i]
        p[position-1]=i
        #As soon as p doesn't contain -1, return the number of minutes! (p will no longer have -1 as soon as the last leaf needed falls)
        if False==(-1 in p):
            return i
    #If you get through the for loop, then some leaf never fell...
    return -1
    

    
    pass




solution(5,[1,5,4,3,2])

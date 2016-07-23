'''You are given two non-empty zero-indexed arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.
The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

int solution(int A[], int B[], int N);
that, given two non-empty zero-indexed arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.'''

#100% solution


def solution(A,B):
    #Let's keep track of how many fish have made it for sure
    survived = 0

    #We'll use the below variable to keep track of upstream moving fish. The upstream moving fish need to fight any downstream moving fish that were more upstream than their position.
    #The downstream moving fish will fight the upstream moving fish in the order of their position...
    #Therefore, we can keep track of these fish with a stack that preserves the order in which a downstream moving fish will fight them!
    injeopardy = []

    #We'll start with the most downstream fish. 
    fish = A.pop()
    direction = B.pop()

#Let's make it so "fish" will only be -1 if and only if there are no more fish with encounters to process.

    while(fish!=-1):
        #If the fish is moving downstream, it needs to battle all of the fish that were moving the other way that were more downstream than it initially
        if direction == 1:
            #At the end of this, the fish will either get eaten of eat all of the fish that it could encounter
            while(fish!=-1 and len(injeopardy)!= 0):
                
                challenger = injeopardy.pop()

                if(fish < challenger):
                    #The downstream moving fish got eaten by the challenger
                    fish = -1
                    #We'll put the surviving fish back on the stack
                    injeopardy.append(challenger)
            
            if fish != -1:
                #The fish made it through all of its possible encounters with upstream moving fish! Let's count it
                survived= survived + 1
                
            
        else:
            #The fish was moving upstream. It will encounter all fish moving downstream. Add it onto the stack
            injeopardy.append(fish)

        try:
            fish = A.pop()
            direction = B.pop()
        except:
            fish = -1

    #All encounters have been accounted for. The surviving fish are the ones that we counted that made it through all their encounters
    #Any fish left on the "injeorpardy" stack are also included
    return survived + len(injeopardy)


        


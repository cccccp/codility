def solution(A):# O(n) time/space complexity
    n=len(A)

    max_left_heights=A[:]
    max_right_heights=A[:]
    
    for i in range(1,n):
        max_left_heights[i]=max(A[i],max_left_heights[i-1])
        
    for i in range(n-2,-1,-1):
        max_right_heights[i]=max(A[i],max_right_heights[i+1])
        
    depth=0
    for i in range(n):
        depth=max(depth, min(max_right_heights[i],max_left_heights[i])-A[i])
        
    return depth

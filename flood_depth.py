def solution(A): #O(n) time/space complexity
    n=len(A)
	# Define the lists of nearest left/right summits (depending on the position i)
    max_left_heights=[A[0]]
    max_right_heights=[A[-1]]
    
    for i in range(1,n):
        max_left_heights.append(max(A[i],max_left_heights[-1]))
        
    for i in range(n-2,-1,-1):
        max_right_heights=[max(A[i],max_right_heights[0])]+max_right_heights
        
    depth=0
    for i in range(n):
        depth=max(depth, min(max_right_heights[i],max_left_heights[i])-A[i])
        
    return depth

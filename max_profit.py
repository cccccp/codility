def solution(A):#O(n) time/space complexity
    n=len(A)
    
    max_values=A[:]
    profit=0
    
    for i in range(n-2,-1,-1):
        max_values[i]=max(max_values[i+1],A[i])
        profit=max(profit,max_values[i]-A[i])
        
    return profit

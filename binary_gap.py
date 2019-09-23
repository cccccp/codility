def solution(N):
    b=bin(N)[2:]
    n=len(b)
    
    maxbinarygap=0
    i=0
    
    while i<n:
        while i<n and b[i]!='0':
            i+=1
        
        j=i
        while j<n and b[j]!='1':
            j+=1
        
        if j<n:
            maxbinarygap=max(maxbinarygap,j-i)

        i=j
        
    return maxbinarygap

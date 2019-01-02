
def recursivesummation(n):
    if n <= 1:
        return n
    return n + recursivesummation(n-1)
    



print(recursivesummation(5))
    

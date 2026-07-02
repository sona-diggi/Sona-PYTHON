def countdown(n):
    if n==0:
        return "done"
    else:
        print(n)
        countdown(n-1)
    
countdown(10)
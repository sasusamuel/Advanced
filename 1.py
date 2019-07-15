numbers = [1,56,234,87,4,76,24,69,90,135]

def is_even (r):
    if r%2 == 0:
        return r
    
print(list(filter(is_even, numbers)))
    
#even numbers with filter
    
print(list(map(lambda r : r%2==0, numbers)))
print (list(filter(lambda r: r%2!=0, numbers)))




   
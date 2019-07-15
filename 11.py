numbers = [1,2,34,5,6,7,8,9]

def is_even (r):
    if r%2 == 0:
        return r
    print(list(filter(is_even, numbers)))

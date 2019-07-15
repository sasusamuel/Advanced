words = ['You, Tube']

def join_strings(strings):
    return reduce (lambda x, y: x + y, strings)
print(join_strings(words))
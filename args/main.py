def add(*args):
    print(type(args))
    print(args)
    return sum(args)

my_sum = add(1, 2, 3, 4)

print(my_sum)
        
# The sum function works with tuples and lists:
a = (1, 2, 3)
print(sum(a))

b = [1, 2, 3]
print(sum(b))

def calculate(n=5, **kwargs):
    print(type(kwargs))
    print(kwargs)


calculate(add=3, multiply=5)
calculate()
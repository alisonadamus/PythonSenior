def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

click = counter()

print(click())
print(click())
print(click())


def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)


print(double(1))
print(double(2))
print(triple(7))
print(triple(8))

print(multiplier(10)(5))


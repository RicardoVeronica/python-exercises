# normal mode
# def fibonacci(n):
#     if n <= 2:
#         return n
#     return fibonacci(n - 1) + (n - 2)


# for number in range(20):
#     print(fibonacci(number + 1))


# buble mode
# def fibonacci(n):
#     a = 0
#     b = 1
#     for number in range(n):
#         c = a + b
#         a = b
#         b = c
#     return b


# for number in range(20):
#     print(fibonacci(number))


# with momoization or cache values
fibonacci_cache = {}  # new empty dict


def fibonacci(n):
    if n in fibonacci_cache:  # if we have cached the value, return it
        return fibonacci_cache[n]

    if n == 1:  # calculate the n term
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value  # cache the value

    return value  # return


for n in range(1, 101):
    print(fibonacci(n))

# fizz buzz problem with list comprehension
fizz = [value for value in range(1, 101) if value % 3 == 0]
buzz = [value for value in range(1, 101) if value % 5 == 0]
FizzBuzz = [value for value in range(1, 101)
            if value % 3 == 0 and value % 5 == 0]


# fizz buzz problem with for
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number} fizzbuzz')
    elif number % 3 == 0:
        print(f'{number} fizz')
    elif number % 5 == 0:
        print(f'{number} buzz')
    else:
        print(number)

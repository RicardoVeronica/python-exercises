# ternary expression
condition = True

x = 1 if condition else 0

print(x)

print('-----')

# separate digits
num1 = 10_000_000_000
num2 =    100_000_000

total = num1 + num2

print(f'This is the total {total:,}')

print('-----')

# count in external text
with open('test.txt', 'r') as my_file:
    files_contents = my_file.read()

words = files_contents.split(' ')
word_count = len(words)

print(f'How many words are in test.txt? Answer: { word_count }')

print('-----')

# for loop with enumerate
names = ['richard', 'ricardo', 'set', 'cain']

for index, name in enumerate(names, start=1):
    print(index, name)

print('-----')

# for loop with zip
names = ['James Logan', 'Clark Kent', 'Charles X. Xavier', 'Bruce Wayne']
heroes = ['Wolverine', 'Superman', 'Professor X', 'Batman']
editorials = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is {hero}')

print('-----')

for name, hero, editorial in zip(names, heroes, editorials):
    print(f'{name} is {hero} for {editorial} comics')

for value in zip(names, heroes, editorials):
    print(value)

print('-----')

# unpack items
# a, b = (1, 2)
items = (1, 2)
a, b = items

a, b, *c, d = (1, 2, 3, 4, 5)

print(f'This is items tuple {items}')
print(f'This is a item: {a}')
print(f'This is b item: {b}')
print(f'This is c item: {c}')  # try to erase this and put this in tuple *_
print(f'This is d item: {d}')

print('-----')

# oop
class Person():
    pass


person = Person()
person.first_name = 'Richard'
person.last_name = 'Veronica'
print(person.first_name)
print(person.last_name)

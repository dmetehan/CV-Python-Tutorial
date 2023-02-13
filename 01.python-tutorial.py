x = 5
y = "computer"
z = 0.2
print(x, y, z)


x, y, z = 5, "computer", 0.2
print(x, y, z)


some_list = [5, "computer", 0.2]
x, y, z = some_list
print(x, y, z)


some_tuple = (5, "computer", 0.2)
x, y, z = some_tuple
print(x, y, z)


some_set = {5, "computer", 0.2}
print(some_set)


some_dict = {'key1': 5, 'key2': "computer", 'key3': 0.2}
print(some_dict)
print(some_dict.keys())
print(some_dict.values())
print(some_dict['key1'])


x, y = 5, 0.2
print(x, "+", y, "=", x + y)
print(f"{x} + {y} = {x+y}")  # formatted strings


sentence = "This course is THE BEST!"
print(sentence)

print(sentence.upper())

print(sentence.lower())

print(sentence.split(' '))

print('-'.join(sentence.split(' ')))


x, y = 5, 10
if x > y:
    print("x > y")
elif x == y:
    print("x == y")
else:
    print("x < y")


for i in range(10):
    print(i)


objects = ["pc", "phone", "wallet"]
for obj in objects:
    print(obj)

for i in range(len(objects)):
    print(i, objects[i])

for i, obj in enumerate(objects):
    print(i, obj)


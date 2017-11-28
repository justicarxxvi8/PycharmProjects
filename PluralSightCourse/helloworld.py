print('Hello World')
name = "Josh"
machine = "HAL"
number = 7
names = ["Mark", "Josh", "Alex"]

print("Nice to meet you {0}. I am {1}".format(name, machine))
print(f"Nice to meet you {name}. I am {machine}")
print(names[-1])

print(names[0:])

if number == 7:
    print("lol")
else:
    print("roflzaho")

if "Mark" in names:
    print("Woof")
else:
    print("Meow")

for name in names:
    print(f"Student name is {name}")

    
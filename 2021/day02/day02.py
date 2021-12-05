def readFile(file):
    with open(file) as file:
        input = file.readlines()
        new_input = []
        for i in input:
            new_input.append(i.strip())
    return new_input


def taskOne(input):
    x = 0
    y = 0
    for i in input:
        if i[0] == "f":
            x += int(i[-1])
        elif i[0] == "d":
            y += int(i[-1])
        elif i[0] == "u":
            y -= int(i[-1])
    return x * y


def taskTwo(input):
    x = 0
    y = 0
    aim = 0
    for i in input:
        if aim < 0:
            aim = 0
        if i[0] == "f":
            x += int(i[-1])
            y += aim * int(i[-1])
        elif i[0] == "d":
            aim += int(i[-1])
        elif i[0] == "u":
            aim -= int(i[-1])
    return x * y


input = readFile("input.txt")

print(taskOne(input))
print(taskTwo(input))

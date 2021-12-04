
def readFile(file):
    with open(file) as file:
        input = file.readlines()
        new_input = []
        for i in input:
            new_input.append(int(i.strip()))
    return new_input


def taskOne(input):
    increments = 0
    for i in range(0, len(input)-1):
        if input[i+1] > input[i]:
            increments += 1
    return increments


input = readFile("input.txt")
print(taskOne(input))

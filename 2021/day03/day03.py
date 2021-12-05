def readFile(file):
    with open(file) as file:
        input = file.readlines()
        new_input = []
        for i in input:
            new_input.append(i.strip())
    return new_input


def taskOne(input):
    gamma = ""
    epsilon = ""
    for i in range(len(input[0])):
        zeroes = 0
        ones = 0
        for j in range(len(input)):
            if int(input[j][i]) == 0:
                zeroes += 1
            elif int(input[j][i]) == 1:
                ones += 1
        if zeroes < ones:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(gamma, epsilon)
    return int(gamma, 2) * int(epsilon, 2)


input = readFile("input.txt")

print(taskOne(input))

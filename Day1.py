elves=[]
elf = 0
largest = [0,0,0]


with open("Day1Input.txt", "r") as file:
    for line in file:
        if line == '\n':
            elves.append(elf)
            elf = 0
        else:
            elf = elf + int(line)
elves.sort(reverse=True)

print(elves[0]+elves[1]+elves[2])




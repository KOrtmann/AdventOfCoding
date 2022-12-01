elves=[]
elf = 0


with open("Day1Input.txt", "r") as file:
    for line in file:
        if line == '\n':
            elves.append(elf)
            elf = 0
        else:
            elf = elf + int(line)

print(max(elves))




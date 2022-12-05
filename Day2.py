win = {"A":"Y", "B":"Z", "C":"X"}
tie = {"A":"X", "B":"Y", "C":"Z"}
lose = {"A":"Z", "B":"X", "C":"Y"}
points = {"X":1 , "Y":2, "Z":3}
score = 0

with open("Day2input.txt", "r") as file:
    for line in file:
        splitline = line.split()
        competitor = splitline[0]
        me = splitline[1]
        if win[competitor] == me:
            score = score + 6
        if tie[competitor] == me:
            score = score + 3

        score = score + points[me]

print(score)


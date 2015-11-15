target = int(input("Please enter a number:"))
runningtotal = 0

for x in range(1, target+1):
    if x % 3 == 0 or x % 5 == 0:
        runningtotal = x + runningtotal

print(runningtotal)

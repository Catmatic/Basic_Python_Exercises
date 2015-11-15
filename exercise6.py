target = int(input("Please enter a number:"))
runningtotal = 0
multiplier = 1

action = input("Shall we compute the sum of '1...n' or the product of '1...n'? Please answer 's' or 'p'.")

if action == "s":
    for x in range(1, target+1):
        runningtotal = x + runningtotal
else:
    runningtotal = 1
    for x in range(1, target+1):
        runningtotal = runningtotal * x
        print(runningtotal)
    

if action == "s":
    print("The sum is", runningtotal)
else:
    print("The product is", runningtotal)

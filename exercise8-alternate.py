#Instead of 8, write a program that takes one number from the user and checks whether it is prime or not

target = int(input("Please input a number to check whether it's prime! \n"))

if len(str(target)) >=8:
    target = int(input("Hey, that number is really big and this algorithm isn't super fast. Try a smaller one?"))
    
if len(str(target)) >=8:
    print("Don't say I didn't warn you. Ctrl-C to interrupt.")

prime = 1

for x in range(2, target):
#    print("{} {} {} = {}".format(target, "%", x, target % x))
#    print(prime)
    if(target % x) == 0:
        prime = 0
        
#print("The value of prime is currently {}".format(prime))
if prime == 1:
    print("Your number is prime!")
else:
    print("Your number is not prime!")

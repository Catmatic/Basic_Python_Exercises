#Write a program that prints the next 20 leap years.

currentyear = int(input("Please enter the current year so I can print the next 20 leap years!\n"))

leapyearlist = []

while len(leapyearlist) < 20:
    if (currentyear % 4 == 0) and (currentyear % 100 != 0) or (currentyear % 400 == 0):
        leapyearlist.append(currentyear)
    currentyear += 1
    
print("The next 20 leap years are: {}".format(leapyearlist))

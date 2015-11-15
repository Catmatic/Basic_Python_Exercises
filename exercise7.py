#Write a program that prints a multiplication table for numbers up to 12.

#I'm sure this can be done better and I'd like to add row and column headers, and a blank space in the top left. I wonder if I'm missing something critical, this problem seems a lot harder than it should be.

rowlist = []
listoflists = []

for x in range(1, 13):
    for y in range(1, 13):
        nextterm = str(x * y).rjust(3)
        rowlist.append(nextterm)
        if y == 12:
            listoflists.append(repr(rowlist))
            rowlist = []
            
for row in listoflists:
    print(row)

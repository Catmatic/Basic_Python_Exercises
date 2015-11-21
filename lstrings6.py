def palindrometest(targetstring):

    """checks whether a given string is a palindrome, ignoring spaces.
    >>>palindrometest("racecar")
    True
    >>>palindrometest("prius")
    False
    >>>palindrometest("mr owl ate my metal worm")
    True
    """

    cleanstring = targetstring.replace(" ", "") 
    negativeindex = -1
    ispalindrome = True 

    for letter in cleanstring:
        #print(cleanstring[negativeindex])
        if letter == cleanstring[negativeindex]:
            negativeindex -=1
        else:
            ispalindrome = False
            break

    return(ispalindrome)

print(palindrometest("racecar"))
print(palindrometest("prius"))
print(palindrometest("mr owl ate my metal worm"))

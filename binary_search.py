#The runtime of this operation is O(log n) - O(n)

def binary_search(target, sorted_list):

  """checks whether a number is present in a sorted list.
  >>>binary_search(5, [1, 2, 4, 6, 7])
  False
  >>>binary_search(5, [1, 2, 4, 5, 7])
  True
  """

#  from sys import setrecursionlimit
#  setrecursionlimit(10)

  guess = sorted_list[int(((len(sorted_list))/2))]
  guessindex = sorted_list.index(guess)

#  print("sorted_list = {}".format(sorted_list))
#  print("guess = {}".format(guess))
#  print("guessindex = {}".format(guessindex))

  if len(sorted_list) == 0 or (len(sorted_list) == 1 and not sorted_list[0] == target):
    return False
  if guess == target:
    return True
  elif guess < target:
    return binary_search(target, sorted_list[guessindex:])
  elif guess > target:
    return binary_search(target, sorted_list[:guessindex])

print(binary_search(5, [1, 2, 4, 5, 7]))
print(binary_search(5, [1, 2, 4, 6, 7]))

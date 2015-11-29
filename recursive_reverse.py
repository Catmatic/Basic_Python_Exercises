def reverse_rec(s):
  """
  Reverse a string, recursively.
  >>>reverse_rec("string"):
  "gnirts"
  """

  if s == "":
      return s
  else:
      return s[-1] + reverse_rec(s[:-1])

print(reverse_rec("string"))

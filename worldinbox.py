def my_new_function(x):
  """Prints messages in boxes.

  >>> my_new_function(['a', 'list', 'of', 'strings'])
  ***********
  * a       *
  * list    *
  * of      *
  * strings *
  ***********
  """
  maxlength = 0
  for word in x:
    if len(word) >= maxlength:
      maxlength = len(word)
  
  print("*" * (maxlength + 4))
  for word in x:
    padding = (maxlength - len(word))
    print("* {}{} *".format(word, (" " * padding)))
  print("*" * (maxlength + 4))

#if _name_ == '__main__':
#  x = 'abc'

my_new_function(['a', 'list', 'of', 'strings'])

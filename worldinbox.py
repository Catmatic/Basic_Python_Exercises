def worldinbox(x):
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
  
  output = "*" * (maxlength + 4) + "\n"
  for word in x:
    padding = (maxlength - len(word))
    output += "* {}{} *".format(word, (" " * padding)) + "\n"
  output += "*" * (maxlength + 4)
  
  return(output)

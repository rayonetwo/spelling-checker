import string

# Read dictionary and return the words as a set.
def get_dict_set(dictionary_file) -> set:
  dict_list = []
  punctuations = string.punctuation.replace("&", "")

  with open(dictionary_file, 'r') as file:
    for line in file.readlines():
      # strip \n and spaces
      line = line.strip()

      # Raise exception if a line has punctuations.
      if len(line) != len(line.strip(punctuations)): raise Exception("Dictionary cannot contain punctuations.")

      # Raise exception if a line has more than one word.
      lineArray = line.split(' ')
      if len(lineArray)>1: raise Exception("Dictionary must contain exactly one word per line.")

      dict_list.append(line.lower())

  dict_set = set(dict_list)

  return dict_set

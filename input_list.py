import string

# Read input_file and return the list of words to spell check.
def get_input_list(input_file) -> list:
  input_list = []
  punctuations = string.punctuation.replace("&", "")

  with open(input_file, 'r') as file:
    input_list=file.read().lower().replace("--", " ").split()

  refined_list = []

  # Remove leading and trailing punctuations from each word.
  for i in input_list:
    i = i.strip(punctuations)
    if i != "": refined_list.append(i)

  # Remove duplicates from the refined input list.
  # refined_list = list(dict.fromkeys(refined_list))

  return refined_list

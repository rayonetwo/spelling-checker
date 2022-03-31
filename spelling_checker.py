from input_list import get_input_list
from dictionary_set import get_dict_set

# Check input_list for words not found in dictionary.
def spell_check(input_file, dictionary_file) -> list:
  input_list = get_input_list(input_file)
  dict_set = get_dict_set(dictionary_file)
  missing_words = []

  for word in input_list:
    unhyphenated = word.split('-')
    for w in unhyphenated:
      if w not in dict_set:
        missing_words.append(word)
        break

  # test output file
  # with open('output', 'w') as file:
  #   file.write(' '.join(missing_words))

  return missing_words

import sys
from spelling_checker import spell_check
# from ascii_check import is_ascii

if __name__=="__main__":
  try:
    # Raise exception if there are more than 2 input files.
    if len(sys.argv) > 3: raise Exception("Cannot pass more than 2 input files from the command line.")

    # Input arguments for files to be read.
    input_file = sys.argv[1]
    dictionary_file = sys.argv[2]

    # Raise exception if either input file contains non-ASCII.
    # if not is_ascii(input_file) or not is_ascii(dictionary_file):
    #   raise Exception("Input files must contain words composed of printable ASCII text.")

    for word in spell_check(input_file, dictionary_file):
      print(word)

  except Exception as e:
    print(str(e))

#usr/bin/python3

from new_word import word_of_list_of_words, word_of_list_of_words_refactor

if __name__ == "__main__":
  print("###########################################")
  print("Running original function tests:")
  print(word_of_list_of_words(["apple", "banana", "cherry"]))  # Output: "aae"
  print(word_of_list_of_words(["dog", "elephant", "frog", "giraffe"]))  # Output: "dloa"
  print(word_of_list_of_words([]))  # Output: ""
  print(word_of_list_of_words(["a", "b", "c", "d", "e"]))  # Output: "a"
  print(word_of_list_of_words(['yoda', 'best', 'has'])) # Output: "yes"
  print("All tests passed.")
  print("###########################################")
  print("")


  print("Running refactored function tests:")
  print(word_of_list_of_words_refactor(["apple", "banana", "cherry"]))  # Output: "aae"
  print(word_of_list_of_words_refactor(["dog", "elephant", "frog", "giraffe"]))  # Output: "dloa"
  print(word_of_list_of_words_refactor([]))  # Output: ""
  print(word_of_list_of_words_refactor(["a", "b", "c", "d", "e"]))  # Output: "a"
  print(word_of_list_of_words(['yoda', 'best', 'has'])) # Output: "yes"
  print("All tests passed.")
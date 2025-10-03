#/usr/bin/python3

from Dictionary import NewDictionary

if __name__ == "__main__":
	print("###########################################")
	print("Running Dictionary class tests:")
  
	# Create an instance of NewDictionary
	my_dict = NewDictionary()
	
	# Test adding new entries
	my_dict.newentry("apple", "A fruit that is red or green.")
	my_dict.newentry("banana", "A long yellow fruit.")
	
	# Test looking up existing entries
	print(my_dict.look("apple"))  # Expected: "A fruit that is red or green."
	print(my_dict.look("banana"))  # Expected: "A long yellow fruit."
	
	# Test looking up a non-existing entry
	print(my_dict.look("cherry"))  # Expected: "Can't find entry for cherry"
	
	# Test adding an entry with missing key
	my_dict.newentry("", "No key provided.")  # Expected: "Key is missing"
	
	# Test adding an entry with missing value
	my_dict.newentry("grape", "")  # Expected: "Value is missing"
	
	print("All tests completed.")
	print("###########################################")
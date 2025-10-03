#/usr/bin/env python3

class NewDictionary():
  "This is a class to add elements to dictionary by methods"

  def __init__(self):
    self._data = {} # Use an internal dictionary to store data

  def newentry(self, key, value):
    if not key:
      print("Key is missing")
    if not value:
      print("Value is missing")
    else:
      self._data[key] = value # Use the internal dictionary for assignment

  def look(self, key):
    if key not in self._data:
      return f"Can't find entry for {key}"
    else:
      # Use the internal dictionary to get the value
      return self._data.get(key)
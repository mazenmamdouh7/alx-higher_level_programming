#!/usr/bin/python3

class MyList(list):
  """MyList class that inherits from list and provides a print_sorted method."""

  def print_sorted(self):
    """Prints the list in ascending sorted order."""
    self.sort()
    print(self)

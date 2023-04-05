#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size

    def get_shoe_size(self):
        print("Getting shoe size...")
        return self._size

    def set_shoe_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_shoe_size, set_shoe_size)
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
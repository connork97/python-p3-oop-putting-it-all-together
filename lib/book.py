#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count

    def get_page_count(self):
        print("Getting page count...")
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# class Book:
#     def __init__(self, title, author="placeholder", page_count="not an integer", genre="non-fiction"):
#         self.title = title
#         self.author = author
#         self.page_count = page_count
#         self.genre = genre

#     def get_page_count(self):
#         print("Getting page count...")
#         return self._page_count
    
#     def set_page_count(self, page_count):
#         if type(page_count) == int:
#             self._page_count = page_count
#         else:
#             print("page_count must be an integer")

#     page_count = property(get_page_count, set_page_count)

# class Book:
#     def __init__(self, book="The World According to Garp"):
#         self.book.title = book.title
#         self.book.author = book.author
#         self.book.page_count = book.page_count
#         self.book.genre = book.genre

#     def get_page_count(self):
#         print("Getting page count...")
#         return self._page_count
    
#     def set_page_count(self, book):
#         if type(book.page_count) == int:
#             self._page_count = book.page_count
#         else:
#             print("page_count must be an integer")

#     page_count = property(get_page_count, set_page_count)
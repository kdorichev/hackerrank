"""
Sample input:

The Alchemist
Paulo Coelho
248
"""
# abc -- Abstract Base Classes
# ABCMeta -- Metaclass for defining Abstract Base Classes
# abstractmethod -- A decorator indicating abstract methods
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        self.price=price
    def display(self):
        print("Title:" , title)
        print("Author:", author)
        print("Price:" , price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

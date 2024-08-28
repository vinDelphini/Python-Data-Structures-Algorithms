# Write a function that takes a list of integers and returns a new list containing 
# only the even numbers from the original list. Do this using a list comprehension.

def evenNumbers(nums):
    return [num for num in nums if num % 2 == 0]

nums = list(range(10))
# print(evenNumbers(nums))


# Write a function that takes a dictionary and returns a new dictionary with keys and values swapped.

def swapDictionaries(dict_):
    dict2 = {}
    for key, value in dict_.items():
        dict2[value] = key
    return dict2

dict_ = {"a": 2, "b": 3}
# print(dict_)
# print(swapDictionaries(dict_))


a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

# Write a function that reads a text file and 
# returns the number of lines, words, and characters in the file
import pandas as pd
pd.read_csv

# Write a function that checks if a given string is a valid email address. 
# Use regular expressions to validate the format
import re
email = "abc@gmail.com"

re.find('@', email)

# Consider two models, Author and Book, in a SQLAlchemy ORM setup. 
# The Author model has a one-to-many relationship with the Book model 
# (i.e., an author can write multiple books). 
# Write a query using SQLAlchemy ORM to find all authors who have written more than three books.
more_than_three_books = Author.objects.annotate(book_count=Count('book')).filter(book_count__gt=3)

# In SQLAlchemy, how would you define two models, Author and Book, 
# where each Author can write multiple Books, but each Book is written 
# by only one Author? Write the SQLAlchemy model classes for this one-to-many relationship

# models.py:

# class Author:

#     id = models.IntegerField()
#     name = models.CharField(length=50)

# class Books(Author):

#     id = OneToMany(Author)
#     book = CharField(length=100)

# In Django, how would you create a custom model manager to filter only the active objects from a model?
#  For example, 
# you have a Product model with a boolean is_active field, 
# and you want to create a manager that returns only the active products



# select * from 
# (select name, COUNT(b.book) as count
# from author a

# left join book b on a.id = b.id
# group by a.name) as subquery

# where count > 3

#  8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_kwargs(name="name1", password="pass1")
print_kwargs(name="name2", password="pass2")
print_kwargs(name="name3", password="pass3")

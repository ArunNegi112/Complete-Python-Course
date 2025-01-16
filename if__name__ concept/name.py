# understanding,   if __name__ == "__main__" :
# when we create a module, like this 'name.py' file

def greet():
    print("Welcome to this cold cold worrldd my brodthar")

greet()      # here, ive called this function, which is a mistake
# cus if i now, import this module in some other file, this function will get called just by importing.

# to avoid this see in 'name2.py'
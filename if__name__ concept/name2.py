def greet():
    return "Welcome to this cold cold worrldd my brodtha"

if __name__ == "__main__":
    print(greet())
# what it does?
# it says that, when executing, if name == main ( the original file (not imported)), only then execute this block

# Hence when importing this module in other file, greet() wont get called until explicitly called
    print(__name__)   # see that it prints "__main__"
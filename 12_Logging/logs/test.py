from logger import logging

def add(a,b):
    logging.debug("The addition process is taking place")
    return a+b


logging.debug("The values in additon function are given")
add(4,5)



# To run this, write, in terminal 
#  cd logs
#  python test.py
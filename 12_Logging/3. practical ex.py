import logging
# Configuring the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    handlers=[
        logging.FileHandler('ex.log'),         # this is another way to create file,using 'handlers'
        logging.StreamHandler()

    ]
    # filename='ex.log',
    # filemode='w'

)


logger = logging.getLogger('Arithmetic app')

def add(a,b):
    logger.debug(f"{a} and {b} are getting added")
    return a+b

def sub(a,b):
    logger.debug(f"{b} is getting subtracted from {a}")
    return a-b

def multiply(a,b):
    logger.debug(f"{a} and {b} are getting multiplied")
    return a+b

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None


print(add(1,2))
print(sub(1,2))
print(multiply(1,2))
print(divide(1,2))
print(divide(1,0))
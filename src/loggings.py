import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Starting the program")

try:
    logging.info("default value giving")

    value=10
    a=int(input("enter the number:"))

    logging.debug("dividing value by a ")
    print(value/a)

except ZeroDivisionError as e:
    logging.warning("zero division log message")
    logging.error("cannot divisible by zero")

finally:
    print("done divisible by zero")
    logging.info("Divison complete")



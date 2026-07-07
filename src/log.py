import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s, %(levelname)s, %(message)s",filename="app1.log",filemode="a")

logging.debug("this is the program start")
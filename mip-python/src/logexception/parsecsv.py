# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
import os
import sys
import logging
import logframework
from UserException import UserException

logger = logging.getLogger('x')
def parse_csv_and_get_columns(filename):
    logger.info("Start:--->Parse CSV")
    logger.debug("Start:--->Parse CSV")
    try:
            count = 0

            csvFile = open(filename, 'r')
            lines = csvFile.readlines()
            for line in lines[1:]:
                val = line.split(",")
                test_str_div = val[0] / val[11]
                print(test_str_div)
                test_zero_div =  (int(val[0]) / int(val[11]))
    except Exception:
        raise UserException("CSV Can not be parsed")

if __name__ == "__main__":
    logframework.setup_logging()
    logger.info("Start:--->Main")
    parse_csv_and_get_columns(filename="D:/Python Proj/mip-python/mip-python/data/flights.csv")

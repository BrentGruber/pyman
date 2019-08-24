import sys
import logging
from .collection import foo


def main():
    """
    Error checking on command line arguments, expecting 1 argument, pathname to a postman collection file
    """
    if len(sys.argv) > 2:
        logging.critical("Too many arguments provided, expecting 1")
        exit()
    elif len(sys.argv) < 2:
        logging.critical("Path to postman collection not provided")
        exit()

    """
    Open the postman json file
    """
    collection_json = open(sys.argv[1], "r")

    """
    Parse the json file into collection object
    """
    foo()

    """
    Close the postman json file
    """
    collection_json.close()

if __name__ == '__main__':
    main()
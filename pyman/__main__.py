import sys
import logging
from related import from_json,to_model
from pyman.models import Collection
from pyman.generator import create_class_template


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
    collection_json = open(sys.argv[1]).read().strip()

    """
    Parse the json file into collection object
    """
    json_dict = from_json(collection_json)
    collection_model = to_model(Collection, json_dict)

    create_class_template(json_dict)

if __name__ == '__main__':
    main()
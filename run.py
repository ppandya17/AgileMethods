import argparse
import os

from src.parser import GEDCOMParser

#authors of the project
__author__ = "Parth Pandya, Malav Shah, Sukanya Rangarajan, Rajat Kinkhabwlal"
__email__ = "ppandya4@stevens.edu, mshah64@stevens.edu, srangar1@stevens.edu, rkinkhab@stevens.edu"

#default file path
FILENAME = 'gedcom_files/Family.ged'


# main function for taking the file path
def main():
    arg_parser = argparse.ArgumentParser()
    action = arg_parser.add_mutually_exclusive_group()
    action.add_argument("-f", "--file", nargs="?", const=FILENAME,
                        default=FILENAME,
                        help="Specify a specific file to run GEDCOM parser on. \
                        Default is " + FILENAME)

    arguments = arg_parser.parse_args()

    path = arguments.file
    if os.path.exists(path):
        individual, families = GEDCOMParser(path)
    else:
        print("[!!] File \"%s\" does not exist.\nExiting..." % path)
        exit(-1)

    printSummary(individual, families)

# function for printing the list of individuals and families to
def printSummary(individual, families):

    for line in individual:
        attrs = vars(line)
        print (', '.join("%s: %s" % item for item in attrs.items()))

    print('----------------------------------------------------------------------------------------------------------------------------------------')
    for line in families:
        attrs = vars(line)
        print (', '.join("%s: %s" % item for item in attrs.items()))

if __name__ == '__main__':
    main()
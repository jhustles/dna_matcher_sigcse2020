import csv
import sys
    # Check for the correct number of command line agruments:

def main():
    # If the command line agruments are not equal to 3, exit the program and show the message
    if len(sys.agrv) != 3:
        sys.exit("Usage: python data.csv sequence.text")

    #Open the DNA database CSV file, read via DictReader
    database = open(sys.argv[1]) # Remember what is open, must be closed later.
    data = csv.DictReader(database)

    dna_file = sys.argv[2]
    with open(dna_file) as f: # with open method closes it on it's own.
        sequence = f.read()
    





main()

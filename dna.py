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
    
    # Instantiate a dictionary data structure to count/track of the target sequence file consecutive DNA STR matches
    counts = {}
    str_keys = data.fieldnames[1:] # Column names in the csv file

    for sub_str in str_keys:
        counts[sub_str] = max_consecutive_matches(sequence, sub_str)

    # Iterate thru each row in the data for matching DNA profile
    for row in data:
        # Extract the current row in the csv file and store in an array for comparison
        extracted_db_row = [int(row[sub_str]) for sub_str in counts]
        # Extract the target strs values from the dictionary and store in an array for comparision
        target = [int(counts[sub_str]) for sub_str in counts]
        # if both arrays counts of consecutive matches for each respective str matches,
        # then print the name from the database, and close the database.
        if target == extracted_db_row:
            print(row['name'])
            database.close()
            return
    # Else, in the event we didn't find a match, print that and close.
    print("No match")
    database.close()
    


def max_consecutive_matches(seq, str):
    pass
    return


main()

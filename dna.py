import csv
import sys

def main():

    # Check for the correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python data.csv sequence.txt")
        sys.exit()

    #Open the dna database csv file and read it using DictReader
    database = open(sys.argv[1]) # Remember to close using this method!
    data = csv.DictReader(database)

    dna_file = sys.argv[2]
    with open(dna_file) as f:
        sequence = f.read()

    # Get the counts for each STR (column titles in the data.csv after "name")
    # Create a dictionary to track counts of target's dna str counts
    counts = {}

    # Extract the database strs from the csv file excluding the name
    str_keys = data.fieldnames[1:]

    # Loop thru each potential STR, return the max consecutive matches, and store them in a dictionary
    for sub_str in str_keys:
        counts[sub_str] = max_consecutive_matches(sequence, sub_str)

    # Check each row in data for matching profile
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

def max_consecutive_matches(sequence, sub_str):
    match_counter = 0
    length = len(sub_str) # Length of each STR from the csvfile

    for i in range(len(sequence)):
        count = 0 # Count consecutive matches
        while True: # while we find a match, we will keep on looping
            start = i + length * count
            end = start + length
            # sequence is an array.
            if sequence[start:end] == sub_str:
                count += 1

            # if we don't find a match we're going to break out of the while loop
            else:

                break
        # match_counter = max(match_counter, count)
        if count > match_counter:
            match_counter = count

    return match_counter


main()
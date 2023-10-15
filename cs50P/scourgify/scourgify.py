"""cs50p Problemset 6 11/10/2023 File I/O"""

import sys
import csv


def main():
    """Entry point"""
    if check_cmd_args():
        read_csv(sys.argv[1])
        # rtn_lst = read_csv(sys.argv[1])
        # for i in rtn_lst:
        #     print(i)

def check_cmd_args():
    """Checks presence of proper cmd-line arguments"""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1], "r") as file:
                data = file.readline
                if data:
                    return True
                else:
                    return False
        except (FileNotFoundError, IndexError):
            sys.exit("Could not read ", sys.argv[1])


def read_csv(file):
    """Reads the csv in sys.argv[1]
    And returns 2 lists based on the csv header one for each column
    """
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader) # read all rows into a list of dictionaries
        
        for row in rows:
            # Access the value of the first column using its header name
            value = row['name']
            
            #perform replace operation
            new_value = value.replace(', ', '')
            
            # update the value in the row
            row['name'] = new_value
            
    # write the modified rows back to the csv file
    fieldnames = csv_reader.fieldnames # get the orignal feildnames
    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()

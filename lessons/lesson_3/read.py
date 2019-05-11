import csv
import os

def open_sample():
    # get the full file path to the csv file
    file_path = (os.path.abspath("tmp/read_from.csv"))
    print(file_path)
    # Read file location, at end of line move to next line
    with open(file_path, newline="") as csvfile:
        # set a variable that references the csv.reader
        # delimiter is how the file is arrange (comma seperated value - csv)
        file_reader = csv.reader(csvfile, delimiter=",")

        count = 0
        # print each row in the file
        for row in file_reader:
            # join statement for items in row
            print(", ".join(row))
            count += 1

    return count

if __name__ == "__main__":
    restult = open_sample()
    print(f'there are {restult} rows')

import csv


def open_sample():

    # Read file location, at end of line move to next line
    with open("tmp/read_from.csv", newline="") as csvfile:
        # set a variable that references the csv.reader
        # delimiter is how the file is arrange (comma seperated value - csv)
        file_reader = csv.reader(csvfile, delimiter=",")

        # print each row in the file
        for row in file_reader:
            # join statement for items in row
            print(", ".join(row))


if __name__ == "__main__":
    open_sample()

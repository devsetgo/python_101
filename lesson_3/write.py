import csv
import datetime


def write_sample():

    count = 1

    # location/file name, overwrite is 'w' and then enter a new line after writing row
    with open("tmp/write_to.csv", "w", newline="") as csvfile:
        file_writer = csv.writer(
            csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        for item in range(0, 10):
            t = datetime.datetime.now()
            write_info = [t, count]
            file_writer.writerow(write_info)
            count += 1

    print("write_sample complete")


def write_sample_append():

    count = 101

    # changing the charter to 'a' makes it append
    with open("tmp/write_to.csv", "a", newline="") as csvfile:
        file_writer = csv.writer(
            csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        for item in range(0, 10):
            t = datetime.datetime.now()
            write_info = [t, count]

            file_writer.writerow(write_info)
            count += 1

    print("write_sample_append complete")


if __name__ == "__main__":
    write_sample()
    write_sample_append()

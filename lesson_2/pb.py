from tqdm import tqdm

# simple loop to count up in a range, but with a simple progress bar
def aLoop():
    count = 0
    # for each item in the range
    for item in tqdm(
        range(0, 10000000), desc="for loop counting", unit=" thing", leave=True
    ):
        # print(count)
        count = count + 1


if __name__ == "__main__":
    aLoop()

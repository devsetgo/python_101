from tqdm import tqdm
import time
# simple loop to count up in a range, but with a simple progress bar

def aLoop():
    t0 = time.time()
    count = 0
    # for each item in the range
    for item in tqdm(
        range(0, 10000000), desc="Count to 10 Million", unit=" thing"):
        # print(count)
        count = count + 1

    t1 = time.time() - t0
    print(f'duration: {t1:.2f} seconds')

if __name__ == "__main__":
    aLoop()

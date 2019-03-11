# To use:
# pip install tqdm (pip3 install tqdm for Mac or Linux)
# tqdm is a progress bar libary for the command line.

from tqdm import tqdm
import time
# simple loop to count up in a range, but with a simple progress bar

def aLoop_Pb():
    t0 = time.time()
    count = 0
    # for each item in the range
    for item in tqdm(
        range(0, 10000000), desc="Count to 10 Million", unit=" a thing"):
        # print(count)
        count = count + 1

    t1 = time.time() - t0
    print(f'duration: {t1:.3f} seconds and counting to {count:,}')

def aLoop_print():
    t0 = time.time()
    count = 0
    # for each item in the range
    for item in range(0, 10000):
        print(f'{count:,}')
        count = count + 1

    t1 = time.time() - t0
    print(f'duration: {t1:.3f} seconds and counting to {count:,}')

def aLoop_none():
    t0 = time.time()
    count = 0
    # for each item in the range
    for item in range(0, 50000000):
        count = count + 1

    t1 = time.time() - t0
    print(f'duration: {t1:.3f} seconds and counting to {count:,}')

if __name__ == "__main__":
    aLoop_print()
    aLoop_Pb()
    aLoop_none()

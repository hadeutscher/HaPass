#!/usr/bin/env python3

import os
import sys
import struct
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Number of random words to generate", type=int)
    parser.add_argument("-e", "--entropy" , help="Size of the password pool", type=int, default=1024)
    parser.add_argument("-t", "--threshold" , help="Word length threshold", type=int, default=3)
    parser.add_argument("-l", "--limit" , help="Word length limit", type=int, default=7)
    args = parser.parse_args()
    if args.entropy < 1000:
        parser.error("Minimum entropy is 1000")
    if args.entropy > 10000:
        parser.error("Maximum entropy is 10000")
    _main(args)

def _main(args):
    with open(r"google-10000-english\google-10000-english.txt", "r") as f:
        opts = f.read().splitlines()
    opts = [opt for opt in opts if args.limit >= len(opt) >= args.threshold]
    opts = opts[:args.entropy]
    print("Generating words out of {0} options...".format(len(opts)))
    print()
    for i in range(args.n):
        n, = struct.unpack("<I", os.urandom(4))
        print(opts[n % len(opts)])

if __name__ == "__main__":
    main()

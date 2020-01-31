import sys


def readLineOfInts():
    line = sys.stdin.readline()
    return [int(word) for word in line.split()]

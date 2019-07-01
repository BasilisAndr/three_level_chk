import os
import subprocess
import re
from string import punctuation
import fileinput

to_read = "../corpora/ckt.crp.txt"
to_write = "../corpora/corpus-stat-res.txt"


def tokenize(line):
    res = []
    for item in line.split():
        if item[-3:] == '...':
            res += [*item[:-3].split('-'), item[-3:]]
        elif item[-1] in punctuation:
            res += [*item[:-1].split('-'), item[-1]]
        else:
            res += item.split('-')
    return res


def main():
    res = []
    for line in fileinput.input():
        wds = tokenize(line)
        print(wds)

if __name__ == '__main__':
    main()

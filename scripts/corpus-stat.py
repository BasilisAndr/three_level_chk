import os
import subprocess
import re
from string import punctuation
import fileinput
FNULL = open('/dev/null', 'w')

to_read = "../corpora/ckt.crp.txt"
to_write = "../corpora/corpus-stat-res.txt"
hfstol = "../ckt.mor.hfstol"
separator = "&"


def tokenize(line):
    res = []
    for item in line.split():
        if item[-1] in punctuation and len(item) == 1:
            res.append(item)
        elif item[-3:] == '...':
            res += [*item[:-3].split('-'), item[-3:]]
        elif item[-1] in punctuation:
            res += [*item[:-1].split('-'), item[-1]]
        else:
            res += item.split('-')
    return res


def gloss(line):
    res = []
    for wd in line:
        out = subprocess.check_output('echo "{}" | hfst-lookup {}'.format(wd, hfstol), shell=True, stderr=FNULL).decode('utf-8')
        analyses = subprocess.check_output('echo "{}" | cut -d"\t" -f2'.format(out, hfstol), shell=True).decode('utf-8')
        res.append(analyses.strip().split('\n'))
    return res




def main():
    res = []
    for line in fileinput.input():
        wds = tokenize(line)
        glosses = gloss(wds)
        print(' '.join([separator.join(x) for x in glosses]))

if __name__ == '__main__':
    main()

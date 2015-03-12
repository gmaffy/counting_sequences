#! usr/bin/env python

def count_seqs(seq):
    count = 0
    for line in seq:
        line = line.lstrip() # strip leading spaces, if any
        if line.startswith('>'):
            count += 1
    return count



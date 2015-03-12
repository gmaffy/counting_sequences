#!/usr/bin/env python

import sys
import os
import seq_utils
import os.path

if len(sys.argv) < 2:
        exit ('gimme a sequence')

direc = sys.argv[1]
for sequences in os.listdir(direc):
        if sequences.endswith('.fasta'):
                seq = open(os.path.join(direc,sequences))
                seq_count = seq_utils.count_seqs(seq)
                print sequences, seq_count



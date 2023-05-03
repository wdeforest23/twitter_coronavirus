#!/usr/bin/env python3

# imports
import os
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter,defaultdict
from glob import glob

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir',required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

inputs = glob(args.input_dir + '/*')

for key in args.keys:
    y_axis = []
    total = defaultdict(lambda: Counter())

    for path in sorted(inputs):
        with open(path) as f:
            tmp = json.load(f)
            tot = 0
            try:
                for k in tmp[key]:
                    tot += tmp[key][k]
            except:
                pass
            y_axis.append(tot)
    plt.plot(np.arange(len(y_axis)), y_axis, label = key)

plt.title('Count of tweets containing specific hashtags by day in 2020')
plt.xlabel('Date in 2020')
plt.xticks([0, 200, 400, 600], ["Jan", "Mar", "Jun", "Sep"])
plt.ylabel('Tweet Count')
plt.legend()
plt.savefig('Alternative_reduce_plot.png')

#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)


#print("items=", items)

x_axis = []
y_axis = []

for x in items[0:10]:
    x_axis.append(x[0])

for y in items[0:10]:
    y_axis.append(y[1])

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

index = range(len(x_axis))[::-1]
plt.bar(index, y_axis)
plt.xticks(index, x_axis)

if args.input_path == "reduced.lang" and args.key == "#coronavirus":
    plt.title(f'Twitter Usage of coronavirus Hashtag by Language in 2020')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'lang_coronavirus_barchart.png')

elif args.input_path == "reduced.lang" and args.key == "#코로나바이러스":
    plt.title(f'Twitter Usage of Korean Hashtag by Language in 2020')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'lang_korean_barchart.png')

elif args.input_path == "reduced.country" and args.key == "#coronavirus":
    plt.title(f'Twitter Usage of coronavirus Hashtag by Country in 2020')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'country_coronavirus_barchart.png')

else:
    plt.title(f'Twitter Usage of Korean Hashtag by Country in 2020')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.show()
    plt.savefig(f'country_korean_barchart.png')

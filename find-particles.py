#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--source', help='Source file, includes full particle path.')
parser.add_argument('--path', help='Path file, includes line number.')
parser.add_argument('--output', help='Outputting file name.')

args = parser.parse_args()

# source_file = open('source.star', mode='r')
# path_file = open('path.star', mode='r')
# output_file = open('output.star', mode='w')

source_file = open(args.source, mode='r')
path_file = open(args.path, mode='r')
output_file = open(args.output, mode='w')

path = []

for i in path_file:
    path.append(int(i.rstrip('\n')))

# path = path_file.readlines()

path_count = 0 # Line number in path file
source_count = 0 # Line number in source file

for j in source_file:
    path_value = path[path_count]
    source_count += 1
    if path_value == source_count:
        output_file.write(j)
        path_count += 1
    
source_file.close()
path_file.close()
output_file.close()
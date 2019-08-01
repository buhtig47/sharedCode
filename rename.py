import argparse
import os

parser = argparse.ArgumentParser(description = 'File Rename Utility')
parser.add_argument("path", type = str, nargs = 2, help = "takes the file path")
args = parser.parse_args()

os.rename(str(args.path[0]), str(args.path[1]))
print('{} renamed to {}'.format(args.path[0], args.path[1]))


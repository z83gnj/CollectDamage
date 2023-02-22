
# Python program to demonstrate
# command line arguments
 
 
import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")
parser.add_argument("-l", "--List", help = "Show list") 
# Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    print("Displaying Output as: % s" % args.Output)

if args.List:
    print("Displaying Output as: % s" % args.List)

# https://docs.python.org/3/library/argparse.html
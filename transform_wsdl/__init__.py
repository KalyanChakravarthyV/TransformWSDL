"""
License: CC0-1.0 (Public Domain)
"""
from transform_wsdl import tri_transform
import sys, getopt


def get_usage():
    return "transform_wsdl <wsdl_location>"


def hello_world():
    print("Hello World!")


def printusage():
    print('tranform_wsdl -i <inputfile> -o <outputfile>')


def tri():
    inputfile = outputfile = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        printusage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printusage()
            sys.exit(1)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if outputfile is None or inputfile is None:
        printusage();
        sys.exit(1)

    # print('Input file is "', inputfile)
    # print('Output file is "', outputfile)

    tri_transform.main(inputfile, outputfile)


if __name__ == "__main__":
    tri()

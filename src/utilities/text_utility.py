import sys


def text_out(output):
    padding = "                                   "
    sys.stdout.write(output + padding)
    sys.stdout.flush()
    sys.stdout.write('\r')
    sys.stdout.flush()

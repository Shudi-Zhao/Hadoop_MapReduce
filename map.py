"""mapper.py"""

import sys
import re
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.lower()
    # remove leading and trailing whitespace
    line = line.strip()
    # replace all special characters with a space
    new_line = re.sub("\W+", " ",line)
    # replace all numbers with a space
    remove_num = re.sub("\d+", " ", new_line)
    # replace the __ with a space
    remove_underscore = re.sub("__", " ", remove_num)
    # split the remove_underscore into words
    words = remove_underscore.split()
    for word in words:
         print '%s\t%s' % (word, 1)
#!/usr/bin/python
# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys
import StringIO

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        # YOUR CODE HERE
        if len(data)!=6:
            continue

        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
        date, time, store, item, cost, payment = data

        # Now print out the data that will be passed to the reducer
        print "{0}\t{1}".format(item, cost)

# test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
# 2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
# 2013-10-09 13:22:59 I/O Error
# ^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
# 1\t2\t3"""

# This function allows you to test the mapper with the provided test string
def main():
	# sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()

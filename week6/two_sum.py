# Algorithms: Design and Analysis Part 1, Coursera
# Week 6 Problem A: Variant of the Two-Sum Problem
# The file contains 500,000 positive integers (there might be some repetitions!).
# Compute the number of target values t in the interval [2500,4000] (inclusive)
# such that there are distinct numbers x, y in the input file that satisfy x+y=t.
'''
    Download the text file here[https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt]. (Right click and save link as).
    
    The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).
    
    The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.
    
    Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
    
    Write your numeric answer (an integer between 0 and 20001) in the space provided.
    
    OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.
'''

import sys

def make_dict(filename):
    """Read in the data stored in the text file and store them into a hash table (Python's dictionary)
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()
    dic = {(int)(elem) for elem in line_list}
    return dic

def findNumTwoSum(dic):
    """Compute the number of target values t in the interval [2500,4000] (inclusive)
    such that there are distinct numbers x, y in the input file that satisfy x+y=t.
    
    Input: dic - a hash table contains all the numbers in the input file"""

    numSatisfied = 0 # the number of target values that passed the requirement
    for target in range(2500, 4001): # [2500, 4000]
        for x in dic:
            y = target - x
            if y in dic and y != x: # ensure dictinctness
                numSatisfied += 1
                break
    return numSatisfied
    
def main():
    dic = make_dict("HashInt.txt")
    print("The number of target values in [2500, 4000] that satisfied the requirement is:", \
              findNumTwoSum(dic))
    
if __name__ == '__main__':
    main()

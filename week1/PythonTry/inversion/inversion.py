# Algorithms: Design and Analysis Part 1, Coursera
# Problem 1: Counting the number of inversions in O(nlogn) time
# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some random order, with no integer repeated. Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
'''
    Download the text file here[http://spark-public.s3.amazonaws.com/algo1/programming_prob/IntegerArray.txt]. (Right click and save link as)
    
    This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
    
    Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
    Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures. The numeric answer for the given input file should be typed in the space below.
    So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.
    (We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)
    
    [TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

'''


def count_inversion(li, c):
    """Count the number of inversions in O(nlogn) time
    li = the original list
    c = a mutable data struct to store the number of inversions"""
    
    length = len(li)
    if length < 2:
        return li
    else:
        middle = int(length / 2)
        return count_split_inversion(count_inversion(li[:middle], c), \
                                     count_inversion(li[middle:], c), c)

def count_split_inversion(left, right, c):
    """Count the number of split inversions, i.e. inversions that occur in both halves of the array.
    left = the left sorted list
    right = the right sorted list
    c = a mutable data struct to store the number of inversions"""
    
    result = []
    while left and right:
        curr = left if left[0] < right[0] else right
        result.append(curr.pop(0))
        if curr == right:
            c[0] += len(left)
    result.extend(left if left else right)
    return result
        
def main():
    count = [0] # a mutable data struct for counting the number of inversions
    f = open('IntegerArray.txt', 'r')
    line_list = f.readlines()
    int_list = [int(line.split()[0]) for line in line_list if line] 
    count_inversion(int_list, count)
    print(count[0])

if __name__ == '__main__':
    main()

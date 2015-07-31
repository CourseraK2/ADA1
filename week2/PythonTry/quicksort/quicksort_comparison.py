# Algorithms: Design and Analysis Part 1, Coursera
# Problem 2: Find the number of comparisons in quicksort in three different pivot-selecting ways: first index, last index, and median of three, respectively
# For this problem, assume way 0 = first index element as pivot, 1 = last as pivot, 2 = median of three as pivot
'''Q1 -
    GENERAL DIRECTIONS:
    
    Download the text file here[http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt].
    
    The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array.
    
    Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
    You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each of the other m−1 elements in the subarray in this recursive call.)
    
    WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).
    
    DIRECTIONS FOR THIS PROBLEM:
    
    For the first part of the programming assignment, you should always use the first element of the array as the pivot element.
    
    HOW TO GIVE US YOUR ANSWER:
    
    Type the numeric answer in the space provided.
    So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.
    (We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)
'''

'''Q2
    
    GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
    
    See the first question.
    
    DIRECTIONS FOR THIS PROBLEM:
    
    Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures. Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.
'''

'''Q3
    
    GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
    
    See the first question.
    
    DIRECTIONS FOR THIS PROBLEM:
    
    Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7, the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).
    
    EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
    
    SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements. You should NOT do this. That is, as in the previous two problems, you should simply add m−1 to your running total of comparisons every time you recurse on a subarray with length m.

'''




def median_of_three(lst, start, end):
    """Returns the index of the median of three values: the first one, the last one, and the middle one.
    lst = input list/array
    start = start index
    end = end index"""

    middle = start + int((end - start) / 2)
    median = min(max(lst[start], lst[end]),
                 max(lst[start], lst[middle]),
                 max(lst[middle], lst[end]))
    if median == lst[start]:
        return start
    elif median == lst[end]:
        return end
    else:
        return middle
        
def partition(lst, start, end, num_comparison, way):
    """Partition the array/list lst around a certain pivot choosing by way
    lst = input list/array
    start = start index
    end = end index
    num_comparison = mutable data struct to store the number of comparisons
    way = which way to select the pivot"""

    if way == 1:
        lst[end], lst[start] = lst[start], lst[end] # exchange last and first
    elif way == 2:
        median_of_three_index = median_of_three(lst, start, end)
        lst[median_of_three_index], lst[start] = lst[start], lst[median_of_three_index]
    else:
        assert way == 0, "Illegal pivot selection way"

    pivot = lst[start]
    i = start + 1
    num_comparison[0] += end - start
    for j in range(start+1, end+1): # indices from start+1 to end
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[start], lst[i-1] = lst[i-1], lst[start]
    return i-1

def quicksort(lst, start, end, num_comparison, way=0):
    """The quicksort algorithm which runs in O(nlogn) time on average
    lst = input list/array
    start = start index
    end = end index
    num_comparison = mutable data struct to store the number of comparisons
    way = which way to select the pivot"""

    if start < end: # if list has 2 or more items
        pivot_index = partition(lst, start, end, num_comparison, way)
        quicksort(lst, start, pivot_index-1, num_comparison, way)
        quicksort(lst, pivot_index+1, end, num_comparison, way)

def main():
    print("Assume 0 = first index, 1 = last index, 2 = median of three as pivot-selection method")
    for way in range(3): # 0, 1, and 2
        f = open('QuickSort.txt', 'r')
        line_list = f.readlines()
        int_list = [int(line.split()[0]) for line in line_list if line]
        num_comparison = [0]
        quicksort(int_list, 0, len(int_list)-1, num_comparison, way)
        print("The number of comparisons in way {0} is".format(way), num_comparison[0])
    
if __name__ == '__main__':
    main()

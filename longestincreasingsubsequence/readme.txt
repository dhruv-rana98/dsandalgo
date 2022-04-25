The main idea is to find the possible number of subsequence which is in increasing order

It is a dynamic programming approach where we start from the end of array which will have only 1 subsequence
as we go towards start , we compare the values and check if the value after the pointer is less than the values after it in increasing order
if it is true, we pick the max value of current value which will be i and 1 + val[i] as we know we can find a subseq in inc order.

First intialise an array with 1 as all the num would have 1 subseq
then to reduce time complexity we can run in backward direction and use the last value to figure out 2nd last.

There are two loops running for comparison therefore the program will have time complexity of n*n = O(N^2).
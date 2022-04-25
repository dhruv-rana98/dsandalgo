# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements 
# without changing the order of the remaining elements.
#  For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

def lengthOfLIS(nums) -> int:
    LIS = [1]*len(nums) #intialise the array with all values a 1
    for i in range(len(nums) - 1, -1 , -1): #loop through the input list
        for j in range(i+1, len(nums)): #loop through the values after i in inc order of j
            if nums[i] < nums[j]: #to check if the subseq form is increasing
                LIS[i] = max(LIS[i], 1 + LIS[j]) #set the i value in output array as found based on condition
    return max(LIS) #we can return the value of i which can form max increasing subseq from input array

print(lengthOfLIS([0,1,0,3,2,3]))
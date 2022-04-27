def twoSum(nums, target):
    hashmap = {} #value: index
    for i in range(len(nums)): #interating through index in nums 
        diff = target - nums[i] #finding diff
        if diff in hashmap: #if diff already in a hashmap 
            return [i, hashmap[diff]] #return current index i and the hashmap index of value
        hashmap[nums[i]] = i #after going through a index value, we add it to the hashmap

print(twoSum([3,4,2], 6))
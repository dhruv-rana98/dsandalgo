# You are given an integer array nums. You are initially positioned at the array's first index,
#  and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

def canJump(nums) -> bool:
        jump = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= jump:
                jump = i
        if jump==0: 
            return True 
        else: 
            return False

print(canJump([3,2,1,0,4]))

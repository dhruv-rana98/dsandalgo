
def search(nums, target):
    l, r = 0, len(nums) - 1
    nums.sort()
    while l<=r:
        mid = (l+r)//2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


searchlist = [12,45,13, 11, 10, 23, 55, 58,44, 50]
print(sorted(searchlist))
print(search(searchlist, 50))



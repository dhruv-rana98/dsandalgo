def containsDuplicate(self, nums) -> bool:
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False
The problem is to solve and return true if there is a duplicate element in the array

The simple splution here is to add element to a hashset and then compare it with the coming characters 
if the char in the set matches another char then return true 
if not matches so have to add the element to the set as it is coming for the firts time
after the loop ends return false which means there was not match.
Time Complexity with hashset is O(1)
therfore with the whole array the time complexity will be O(N) where n is the size of the input array
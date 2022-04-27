Refer the video https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode

Start by creating hashmap 
As we cannot use the value we visited for the target sum we will first compute the difference 
with the value and the target and check whether the remainder is in hashmap,
if it is then we return the index of both elements
else we add the value to the hashmap and then move on to next value in the array

As with hashmap inserting is O(1), comparing is O(1)
and then we are performing it on a array 
TX = O(N) Where N is the size of array
SX = O(N) Where N is no of elements in hashmap
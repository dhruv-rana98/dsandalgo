Need to use the dynamic programming approach
construct a 2d Matrix with row as text1 and column as text2
start from top and track when the word matches, go diagonally down
if word does not match look adjacent left and down
go through the same until you hit the last word
keep value as 0 for 1 row and 1 column which will be out of bound

Solution
Now to traceback to the fist place iterate through a for loop and start from bottom
if character matches then add 1 to the value which is diagonal to the current position
if value does not match then put the max value from two adjacent position to the current position
continue till you reach the start or at the top
finally you can return the first position which is arr[0][0] which will return the length of longest subsequence. 
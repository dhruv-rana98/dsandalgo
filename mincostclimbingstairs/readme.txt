This problem has a dynamic programming approach
We have to find the min value of stairs we can take to reach the destination above the last stair.

We start from end by appending the last value of stair as 0 as we dont need any value to add
we start from the previous last and add the value of min of two steps achievable trough the value as after
giving the cost we can either take one step or two step

We find cost from rev
last index cost is 0
last 2nd index cost can be index val + 0 and index value + (index of last val + 1)(which is out of bound)
we start with last 3rd index whose total will be val of index + min val(index[curent+1]{1st step},index[current+2]{direct 2nd step})

In the same manner we will find distance of all nodes to the top so finally when we reach start we can easily derive it.
Finally we can start with 0th or 1st index. So we return min value frm 0th or 1st index.
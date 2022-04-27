def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False #return if the lengths of string are not equal
    
    countS, countT = {}, {} #initialise hashmap 
    
    for i in range(len(s)):  #use of the for loop to build both the hashmaps
        countS[s[i]] = 1 + countS.get(s[i], 0)  #use of get method to overcome key error in case of no key 
                                                #and give result as 0 for the error
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:  #comparing the values 
        if countS[c] != countT.get(c, 0): #check if any of the key value mismatches then return false
            return False
    return True


print(isAnagram("rat","car"))
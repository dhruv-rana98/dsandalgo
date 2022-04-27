Two strings are said to be anagram if both the strings have same occurences of same characters but the ordering is different

The first approach to solve is to sort both the strings and compare and retun the result

the second approach is to use python counter which will generate as hashmap of characters

the third approach is to create two hashmaps of both the string and then interate thrugh the 1st string 
hashpmap and compare with the key value of the second string hashmap and if all matches are true return true

TX = O(m + t) where m and t are both the size of strings
sx = O(m + t) where m and t are both the size of hashmaps
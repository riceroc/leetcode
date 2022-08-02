class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                    
        # check if length of strings are not equal
        if len(s) != len(t):
            return False
        
        # initialize empty hash maps
        countS, countT = {}, {}

        # iterate through the length of any string
        for i in range(len(s)):
            # get key value with get method for error handling 
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)

        # check if counts are not equal
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

                
        # easy 1-liner with Counter method
        # return Counter(s) == Counter(t)
        
        return True


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## Brute force - range over. Time: O(n**2) Space: O(n)
        
        
        ## Sorting - sort the array first, then iterate over neighbors using Pointers. 
        ## Time: O(nlogn). Space 
        
        
        ## Hash Map/Set - 
        
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
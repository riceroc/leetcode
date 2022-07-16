class Solution:
    def climbStairs(self, n: int) -> int:
        pointer1, pointer2 = 1, 1
        
        for i in range(n - 1):
            temp = pointer2
            pointer1 = pointer1 + pointer2
            pointer2 = temp
        return pointer1
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Let dp[i] be the min cost to reach the i_th floor.
        # to reach the i_th floor we have 2 ways:
        # Jump 1 step from (i-1) floor, last floor to final, dp[i]=dp[i-1] + cost[i-1]
        # Jump 2 steps from (i-2) floor, 2nd to last floor to final, dp[i]=dp[i-2] + cost[i-2]
        # dp[i] = min cost between 2 above methods
        # dp[n] = min cost to reach the top floor
        
        n = len(cost)
        dp = [0] * (n+1) # dp[i] is min cost to reach the i_th floor
        for i in range(2, n+1):
            jumpOne = dp[i - 1] + cost[i - 1] # min cost if we jump 1 step from last step
            jumpTwo = dp[i - 2] + cost[i - 2] #min cost if we jump 2 steps from 2ndtolast step
            dp[i] = min(jumpOne, jumpTwo)
        return dp[n]
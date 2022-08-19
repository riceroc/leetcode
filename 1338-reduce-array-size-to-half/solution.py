class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()
        
        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans = ans + 1
            removed = removed + frequencies.pop()
        return ans
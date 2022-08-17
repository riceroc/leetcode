class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                dict[c] = i
                seen.add(c)
            elif c in dict:
                del dict[c]
        return next(iter(dict.values())) if dict else -1
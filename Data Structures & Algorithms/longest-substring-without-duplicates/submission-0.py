class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        diff = set()
        left = 0
        maxL = 0

        for right in range(len(s)):

            while s[right] in diff:
                diff.remove(s[left])
                left += 1
            diff.add(s[right])

            maxL = max(maxL, right - left + 1)

        return maxL



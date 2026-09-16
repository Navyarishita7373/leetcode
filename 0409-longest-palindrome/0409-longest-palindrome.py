class Solution(object):
    def longestPalindrome(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        ans = 0
        odd = False

        for value in count.values():
            ans += (value // 2) * 2

            if value % 2 == 1:
                odd = True

        if odd:
            ans += 1

        return ans
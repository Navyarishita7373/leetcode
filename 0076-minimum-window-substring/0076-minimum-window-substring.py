from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        window = {}

        left = 0
        formed = 0
        required = len(need)

        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]
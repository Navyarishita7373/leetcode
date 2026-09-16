class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        total = sum(arr[:k])

        if total >= k * threshold:
            count += 1

        for i in range(k, len(arr)):
            total += arr[i]
            total -= arr[i - k]

            if total >= k * threshold:
                count += 1

        return count
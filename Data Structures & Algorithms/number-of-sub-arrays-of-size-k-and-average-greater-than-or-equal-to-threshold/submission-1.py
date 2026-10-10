class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # start, end representing the boundary of SW
        start = end = 0

        # answer for valid counts
        answer = 0
        sum = 0

        # iterate the array, count the valid subarray
        # if window reached, move the window ahead
        while end < len(arr):
            while abs(start - end) < k:
                sum += arr[end]
                end += 1
            
            if sum/k >= threshold:
                answer += 1
                    
            sum -= arr[start]
            start += 1

        return answer
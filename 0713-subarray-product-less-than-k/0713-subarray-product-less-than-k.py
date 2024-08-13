class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        l = 0
        curProduct = 1
        for r in range(len(nums)):
            curProduct *= nums[r]
            while curProduct >= k:
                curProduct /= nums[l]
                l += 1
            ans += r - l + 1
        return ans
        
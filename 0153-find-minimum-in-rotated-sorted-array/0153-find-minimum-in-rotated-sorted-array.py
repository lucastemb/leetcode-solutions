class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        small=float("infinity")
        while start < end:
            mid=(start+end)//2
            small=min(small,nums[mid])
            if nums[mid] > nums[end]:
                start=mid+1
            else:
                end=mid-1

        return min(small,nums[start])
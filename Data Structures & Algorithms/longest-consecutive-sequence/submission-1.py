class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        count = 1
        pointer = 0
        maxy = 1

        while pointer < len(nums)-1:
            i = pointer + 1
            if nums[i] - nums[pointer] == 1:
                count +=1
            else:
                count = 1
            maxy = max(maxy, count)
            pointer+=1

        return maxy


        


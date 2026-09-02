class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix = [1]
        pos_fix = [1]
        res = []
        nums_rev = reversed(nums)
        for i in nums:
            pre_fix.append(pre_fix[-1] * i)
        for i in nums_rev:
            pos_fix.append(pos_fix[-1] * i)
        pos_fix_rev =  list(reversed(pos_fix))
        
        for i in range(len(nums)):
            temp = pre_fix[i] * pos_fix_rev[i+1] 
            res.append(temp)

        return res




        




        
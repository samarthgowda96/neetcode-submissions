class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       d = {}
       res = []
       for i in nums:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i]+=1
       #print(d)
       res = sorted(d, key=d.get, reverse=True)
   
       
       return res[:k]
        
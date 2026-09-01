class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for i in strs:
            s = "".join(sorted(i))
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        
        for k, v in d.items():
            res.append(v)
        return res

        

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for i in strs:
            s = sorted(i)
            if "".join(s) not in d:
                d["".join(s)] = [i]
            else:
                d["".join(s)].append(i)
        
        for k, v in d.items():
            res.append(v)
        return res

        

        
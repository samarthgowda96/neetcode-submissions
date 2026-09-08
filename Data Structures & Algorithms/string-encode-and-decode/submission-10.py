class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"$"+ s
        return res 


    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        temp = ""
        while l < len(s):
            if s[l].isnumeric():
                temp += s[l]
                l += 1
            elif s[l] == "$":
                l+=1
                leng = l+int(temp)
                res.append(s[l:leng])
                l =leng
                temp = ""
        return res

                

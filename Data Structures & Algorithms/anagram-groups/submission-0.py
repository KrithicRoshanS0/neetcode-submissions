class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            f=[0 for _ in range(26)]
            for j in i:
                f[ord(j)-97]+=1
            key=tuple(f)
            if key not in d:
                d[key]=[]
            d[key].append(i)
        l=[]
        for i in list(d.keys()):
            l.append(d[i])
        return l
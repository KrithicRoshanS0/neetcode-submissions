class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(s):
            d={}
            for i in s:
                d[i]=d.get(i,0)+1
            return d
        d1,d2={},{}
        d1=freq(s)
        d2=freq(t)
        return d1==d2
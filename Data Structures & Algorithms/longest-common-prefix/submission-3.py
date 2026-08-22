class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(1,len(strs)):
            j=0
            while j < (min(len(strs[i]), len(a))):
                if a[j]!=strs[i][j]:
                    break
                j+=1
            a=a[:j]
        return a

        
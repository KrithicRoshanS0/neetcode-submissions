class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=0
        n=0
        a=0
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                n+=1
            else:
                if n+1>m:
                    m=n+1
                    a=nums[i]
                    n=0
        return nums[-1] if n+1>m else a

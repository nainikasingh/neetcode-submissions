class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # list1=sorted(nums)
        # for i in range(0,len(list1)-1):
        #     if list1[i]==list1[i+1]:
        #         return True
        #     else:
        #         i+=1
        # return False
        return len(set(nums)) < len(nums)

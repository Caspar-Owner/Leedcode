class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            if  (target - nums[i] ) in nums:
                for x in range(len(nums)):
                    if i == x:
                        pass
                    elif target == nums[i] + nums[x]:
                        return i , x
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        


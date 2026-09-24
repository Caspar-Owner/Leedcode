class Solution(object):
    def smallestIndex(self, nums):
        self.nums = nums

        for num_location in range(len(nums)):

            location = nums[num_location]
            if len(str(nums[num_location])) > 1:
                location = 0
                for x in str(nums[num_location]):
                    location += int(x)

            if location == num_location:
                return num_location         
        return -1
class Solution(object):
    def removeElement(self, nums, val):
        xx = 0

        for i in nums:
            if i != val:
                nums[xx] = i
                xx += 1
        return xx
# the valid element only goes to [ xx ]
# if nums was = [1.3.4.1,1,5] and val = 1
# it will change change nums = [3,4,5,1,1,5]

# output = 3
# it will only read in out till 3 output
# [3,4,5]
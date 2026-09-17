class Solution(object):
    def removeElement(self, nums, val):
        xx = 0

        for i in nums:
            if i != val:
                nums[xx] = i
                xx += 1
        return xx

# class Solution(object):
#     def removeElement(self, nums, val):
#         x = 0

#         for xy in nums:
#             if xy != val:
#                 nums[x] = xy
#                 x += 1
#         return x
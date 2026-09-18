class Solution(object):
    def plusOne(self, digits):
        num = ""
        i = []
        for x in digits:
            num += str(x)
        num = int(num) + 1
        for x in str(num):
            i.append(int(x)) 
        return i
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
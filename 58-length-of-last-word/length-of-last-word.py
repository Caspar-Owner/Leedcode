class Solution(object):
    def lengthOfLastWord(self, s):
        x = True
        y = 1
        a = ""
        while x :
            a = s.split(" ")[-y]
            if len(a) > 0:
                x = False
            y += 1
        return len(a)
        """
        :type s: str
        :rtype: int
        """
        
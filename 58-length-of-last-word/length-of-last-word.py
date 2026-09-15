class Solution(object):
    def lengthOfLastWord(self, s):
        x = True
        y = 1
        while x :
            a = s.split(" ")[-y]
            if len(a) > 0:
                x = False
            y += 1
        return len(a)
class Solution(object):
    def romanToInt(self, s):
        self.s = s
        int_s = 0
        for roman in self.s:
            if roman == "I":
                int_s += 1
            elif roman == "V":
                int_s += 5
            elif roman == "X":
                int_s += 10
            elif roman == "L":
                int_s += 50
            elif roman == "C":
                int_s += 100
            elif roman == "D":
                int_s += 500
            elif roman == "M":
                int_s += 1000
        if "IV" in self.s:
            int_s -= 2
        if "IX" in self.s:
            int_s -= 2 
        if "XL" in self.s:
            int_s -= 20 
        if "XC" in self.s:
            int_s -= 20
        if "CD" in self.s:
            int_s -= 200
        if "CM" in self.s:
            int_s -= 200
        return int_s
        """
        :type s: str
        :rtype: int
        """
        
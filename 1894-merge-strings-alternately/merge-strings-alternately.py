class Solution(object):
    def mergeAlternately(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        word1_2 = ""

        loop_run = 0
        if len(word1) < len(word2):
            loop_run += len(word2)
        elif len(word1) > len(word2):
            loop_run += len(word1)
        else:
            loop_run += len(word1)

        for x in range(loop_run):
            try:
                word1_2 += self.word1[x]
            except:
                pass
            try:
                word1_2 += self.word2[x]
            except:
                pass
        return word1_2
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
class Solution(object):
    def longestCommonPrefix(self, strs):
        # same_word = ""
        # num_len = len(strs)
        # for x in strs[0]:
        #     # same_word += x
        #     ox  = 0
        #     for a in range(len(strs)):
        #         if x in strs[a]:
        #             ox += 1
        #             if ox == len(strs):
        #                 same_word += x


        # return same_word
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix
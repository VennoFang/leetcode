__author__ = 'Venno'
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    def isIsomorphic(self, s, t):
        if self.match(s) == self.match(t):
            return True
        else:
            return False

    def match(self, s):
        if s == "":
            return [0]
        dic = {}
        re = []
        count = 1
        for i in range(0, len(s)):
            if s[i] in dic:
                re.append(dic[s[i]])
            else:
                dic[s[i]] = count
                re.append(count)
                count += 1
        return re





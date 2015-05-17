__author__ = 'Venno'
class Solution:
    # @param {string} s
    # @return {boolean}
    def check(self, temp):
        left = 0
        right = len(temp)-1
        while left < right:
            if temp[left] != temp[right]:
                return False
            else:
                left +=1
                right -=1
        return True
    def isPalindrome(self, s):
        if s == '':
            return True
        else:
            temp = ''
            s=list(s)
            count = 0
            for i in range(0, len(s)):
                if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                    s[i] = chr(ord(s[i])-32)
                if (ord(s[i])>=48 and ord(s[i])<=57) or (ord(s[i])>=65 and ord(s[i])<=90):
                    s[count]=s[i]
                    count+=1
                i+=1
            temp = s[:count]
            return self.check(temp)

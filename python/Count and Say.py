__author__ = 'Venno'
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        result = '1'
        s = ['1']
        if n == 1:
            return result
        for i in range(2, n):
           start = 0
           temp = []
           while start < len(s):
               count = 1
               next = start +1
# unfinished


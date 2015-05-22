__author__ = 'Venno'
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        cycle = set()
        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1

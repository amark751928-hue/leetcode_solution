class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        if n>=1000:
            x+=n-1000+1
        if n>=10**6:
            x+=n-10**6+1
        if n>=10**9:
            x+=n-10**9+1
        if n>=10**12:
            x+=n-10**12+1
        if n>= 10**15:
            x+=n-10**15+1
        return x
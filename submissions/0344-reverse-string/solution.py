class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0 
        while i < len(s)//2: 
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp
            i += 1
        

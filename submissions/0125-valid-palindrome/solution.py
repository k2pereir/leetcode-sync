class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new = ""
        for i in range(len(s)): 
            if s[i].isalnum(): 
                new = new + s[i]
        i = 0 
        while i < len(new):
            if new[i] != new[len(new) - i - 1]: 
                return False 
            i += 1
        return True


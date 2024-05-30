class Solution(object):
    def isPalindrome(self, x):
        num = str(x) 
        numlist = [int(char) if char.isdigit() else char for char in num]
        reverse = numlist[::-1]
        l = len(numlist)
        counter = 0
        
        for i in range(len(numlist)):
            if numlist[i] == reverse[i]:
                counter = counter + 1

        
        return counter == len(numlist)
        
        """
        :type x: int
        :rtype: bool
        """
        

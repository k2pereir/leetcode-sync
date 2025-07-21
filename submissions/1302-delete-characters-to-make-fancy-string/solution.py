class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        temp = list()
        length = len(s)
        max = 2
        count = 0
        for i in range(length): 
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count <= max:
                temp.append(s[i])
        return ''.join(temp)
        

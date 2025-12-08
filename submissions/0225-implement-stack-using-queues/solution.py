class MyStack(object):

    def __init__(self):
        self._data = []
        self._size = 0
        self._latest = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._data.append(x)
        self._size += 1

    def pop(self):
        """
        :rtype: int
        """
        if self._size != 0: 
            val = self._data.pop(self._size - 1)
            self._size -= 1
            return val

    def top(self):
        """
        :rtype: int
        """
        if self._size != 0: 
            val = self._data[self._size - 1]
            return val
        

    def empty(self):
        if self._size == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

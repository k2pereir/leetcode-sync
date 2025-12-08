class MyQueue(object):

    def __init__(self):
        self._data = list()
        self._size = 0 
        

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
            val = self._data.pop(0)
            self._size -= 1
            return val
        

    def peek(self):
        """
        :rtype: int
        """
        if self._size != 0:
            return self._data[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self._size == 0: 
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class Counter:
    def __init__(self, count = 0, step = 1):
        self.count = count
        self.step = step

    def increment(self):
        '''Increments the count by the step'''
        self.count += self.step

    def decrement(self):
        '''Decrements the count by the step'''
        self.count -= self.step

    def reset(self):
        '''Sets the count back to 0'''
        self.count = 0

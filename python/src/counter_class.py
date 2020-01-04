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

    def export_info(self, filename: str = "*.cnt"):
        '''Writes the count and step size to a file'''
        file = open(filename, "w")
        file.write("{}\n{}".format(self.count, self.step))
        file.close()

    def import_info(self, filename:str = "*.cnt"):
        '''Reads the count and step size from a file'''
        file = open(filename, "r")
        self.count = int(file.read(1))
        file.read(1)
        self.step = int(file.read(1))
        file.close()


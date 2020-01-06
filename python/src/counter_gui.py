#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
from counter_class import Counter

class GUI:
    def __init__(self, size:str, memory:str):
        self.root = tkinter.Tk()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    GUI().run()

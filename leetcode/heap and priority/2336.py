'''
I dont see any point
'''

class SmallestInfiniteSet(object):

    def __init__(self):
        self.elements = set()
        self.l = 1

    def popSmallest(self):
        if self.elements:
            t = min(self.elements)
            self.elements.discard(t)
            return t
        else:
            self.l += 1
            return self.l - 1
                

    def addBack(self, num):
        if num < self.l:
            self.elements.add(num)
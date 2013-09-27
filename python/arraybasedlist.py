"""
An abstract superclass for all array-based lists

Subclasses of this must implement get(i), set(i,x), add(i,x), remove(i)
and size()
"""
import random

class ArrayBasedList(object):
    def __str__(self):
        return str([self.get(i) for i in range(self.size())])

    def __len__(self):
        return self.size()

    def append(self, x):
        self.add(self.size(), x)

    def clear(self):
        while self.size() > 0:
            self.remove(self.size()-1)

    def new_array(self, n):
        return [None]*n

    def insert(i, x):
        self.add(i, x)

    def __eq__(self, a):
        if len(a) != len(self): return False
        for i in range(len(a)):
            if (a[i] != self.get(i)): return False
        return True

    def __ne__(self, a):
        return not self == a

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def test(self):
        a = list()
        self.clear()

        for k in range(5):
            for i in range(20):
                a.append(i)
                self.append(i)

            print "list = " + str(a)
            print "self = " + str(self)

            for i in range(20, 1000):
                j = random.randrange(len(a)+1)
                a.insert(j, i)
                self.add(j, i)
                assert self == a;


            while len(a) > 0:
                j = random.randrange(len(a))
                del a[j] 
                self.remove(j)
                assert self == a;



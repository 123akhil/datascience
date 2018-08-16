class Queue(object):


    def __init__(self):

        self.vals = []
        
    def insert(self,value):

        self.vals.append(value)

    def remove(self):

        try:
        
            last = self.vals[0]

            del self.vals[0]

            return last

        except IndexError:

            raise ValueError


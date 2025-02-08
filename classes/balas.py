from random import choice

class Balas():
    def __init__(self,balas):
        self.balas = []
        for x in range(0,balas):
            self.balas += [1]
        for x in range(0,6-balas):
            self.balas += [0]
        
    
    def escolhe(self) -> int:
        b = choice(self.balas)
        for i,n in enumerate(self.balas):
            if n==b:
                self.balas.pop(i)
                return n
        return 2


class transaction:
    def __init__(self, mode, kitol, kinek, osszeg) -> None:
        self.mode = mode
        self.kitol = kitol
        self.kinek = kinek
        self.osszeg = osszeg


    def getTransaction(self):
        return [self.mode, self.kitol, self.kinek, self.osszeg]

import collections

# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:

    def __init__(self, skus):
        self.skus = skus
        self.items = None
        self.validItems = ['A', 'B', 'C', 'D']


    def validateInput(self) -> bool:
        if not isinstance(self.skus, str):
            return False
        
        for i in self.skus:
            if i not in self.validItems:
                return False
        
        return True

        

    def countSKUS(self) -> None:
        self.items = collections.defaultdict(int)

        for i in self.skus:
            self.items[i]+=1



def checkout(skus):
    





